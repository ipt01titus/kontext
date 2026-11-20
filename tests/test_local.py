import copy
import json
import tempfile
import threading
import unittest
import urllib.request
import urllib.error
from concurrent.futures import ThreadPoolExecutor
from unittest.mock import patch
from app.storage import Store, Invalid, Conflict
from app.server import make_server

def fixture():
    return dict(schema=1, hierarchyVersion=1, nextNumber=8,
        projects=[dict(id='p',name='Projekt',number=2,color='#4b8267',parent=None)],
        people=[dict(id='urs',name='Urs Müller',number=1,projects=['p'],emails=[],phones=[],trust=None,extra={})],
        objects=[dict(id='a',name='Gartenhaus',number=3,projects=['p'],parent=None),dict(id='b',name='Elektrik',number=4,projects=['p'],parent='a')],
        tasks=[dict(id='t',name='Elektrik planen',number=5,projects=['p'],owner='urs',status='open',targets=[dict(type='object',id='b')],goals=['g'],predecessors=[],steps=[dict(text='Prüfen',done=False)],comments=[dict(author='urs',text='Erhalten',at='2026-11-20T10:00:00Z')])],
        goals=[dict(id='g',name='Nutzbar',number=6,projects=['p'],people=['urs'],objects=['a'])],
        events=[dict(id='e',name='Besprechen',number=7,date='2026-11-20',projects=['p'],people=['urs'],objects=['a'],goals=['g'],tasks=['t'])])

class StoreTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory();self.addCleanup(self.temp.cleanup)
        self.store=Store(self.temp.name);self.state=fixture()
        self.store.save('own',self.state,0,'initial')

    def test_reopen_preserves_ids_numbers_relationships_and_comments(self):
        loaded=Store(self.temp.name).load('own')
        self.assertEqual(loaded['state'],self.state)
        self.assertEqual(loaded['revision'],1)

    def test_cancel_reopen_and_restore_preserve_task_and_relationships(self):
        cancelled=copy.deepcopy(self.state);cancelled['tasks'][0]['status']='cancelled'
        self.store.save('own',cancelled,1,'cancel')
        self.assertEqual(Store(self.temp.name).load('own')['state'],cancelled)
        backup=self.store.backup()
        reopened=copy.deepcopy(cancelled);reopened['tasks'][0]['status']='open'
        self.store.save('own',reopened,2,'reopen')
        self.assertEqual(self.store.load('own')['state'],reopened)
        self.assertEqual(self.store.restore('own',backup,3,'restore-cancelled')['state'],cancelled)

    def test_lost_response_retry_is_idempotent_and_stale_edit_conflicts(self):
        self.assertEqual(self.store.save('own',self.state,0,'initial')['revision'],1)
        changed=copy.deepcopy(self.state);changed['tasks'][0]['name']='Geändert'
        with self.assertRaises(Invalid):self.store.save('own',changed,0,'initial')
        with self.assertRaises(Conflict):self.store.save('own',changed,0,'stale')
        self.assertEqual(self.store.load('own')['state'],self.state)

    def test_restore_creates_a_safety_backup_and_preserves_number_highwater(self):
        backup=self.store.backup()
        changed=copy.deepcopy(self.state);changed['tasks'][0]['name']='Später';changed['nextNumber']=20
        self.store.save('own',changed,1,'change')
        count=len(self.store.list_backups())
        result=self.store.restore('own',backup,2,'restore')
        self.assertEqual(result['state']['tasks'],self.state['tasks'])
        self.assertEqual(result['state']['nextNumber'],20)
        self.assertEqual(result['revision'],3)
        self.assertEqual(len(self.store.list_backups()),count+1)

    def test_backup_failure_does_not_acknowledge_or_modify_data(self):
        changed=copy.deepcopy(self.state);changed['tasks'][0]['name']='Neu'
        with patch.object(self.store,'_backup',side_effect=OSError('disk full')):
            with self.assertRaises(OSError):self.store.save('own',changed,1,'retry')
        self.assertEqual(self.store.load('own')['state'],self.state)
        self.assertEqual(self.store.save('own',changed,1,'retry')['revision'],2)

    def test_invalid_graph_and_numbers_leave_saved_data_untouched(self):
        bad=copy.deepcopy(self.state);bad['objects'][0]['parent']='b'
        with self.assertRaises(Invalid):self.store.save('own',bad,1,'cycle')
        bad=copy.deepcopy(self.state);bad['tasks'][0]['number']=3
        with self.assertRaises(Invalid):self.store.save('own',bad,1,'number')
        bad=copy.deepcopy(self.state);bad['tasks'][0]['targets'][0]['id']='missing'
        with self.assertRaises(Invalid):self.store.save('own',bad,1,'missing')
        self.assertEqual(self.store.load('own')['revision'],1)

    def test_demo_is_separate_and_regular_edits_cannot_renumber_records(self):
        demo=copy.deepcopy(self.state);demo['tasks'][0]['name']='Demo'
        self.store.save('demo',demo,0,'demo')
        self.assertEqual(self.store.load('own')['state'],self.state)
        bad=copy.deepcopy(self.state);bad['tasks'][0]['number']=8;bad['nextNumber']=9
        with self.assertRaises(Invalid):self.store.save('own',bad,1,'renumber')

    def test_competing_store_instances_do_not_lose_a_committed_write(self):
        second=Store(self.temp.name);barrier=threading.Barrier(2)
        def save(store,name):
            changed=copy.deepcopy(self.state);changed['tasks'][0]['name']=name
            barrier.wait()
            try:store.save('own',changed,1,name);return 'saved'
            except Conflict:return 'conflict'
        with ThreadPoolExecutor(2) as pool:
            outcomes=list(pool.map(lambda pair:save(*pair),[(self.store,'one'),(second,'two')]))
        self.assertEqual(sorted(outcomes),['conflict','saved'])
        self.assertEqual(self.store.load('own')['revision'],2)

    def test_restore_rejects_path_traversal(self):
        with self.assertRaises(Invalid):self.store.restore('own','../kontext.sqlite3',1,'restore')

class HttpTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory()
        self.server=make_server(self.temp.name,0)
        self.thread=threading.Thread(target=self.server.serve_forever,daemon=True);self.thread.start()
        self.url='http://127.0.0.1:'+str(self.server.server_port)
    def tearDown(self):
        self.server.shutdown();self.server.server_close();self.thread.join();self.temp.cleanup()
    def post(self,payload,origin=None):
        req=urllib.request.Request(self.url+'/api/state',data=json.dumps(payload).encode(),headers={'Content-Type':'application/json','Origin':origin or self.url,'X-Kontext-Client':'1'},method='POST')
        with urllib.request.urlopen(req) as response:return json.load(response)
    def test_save_export_and_restart_persist_without_external_services(self):
        saved=self.post(dict(workspace='own',state=fixture(),revision=0,operationId='http-save'))
        self.assertEqual(saved['revision'],1)
        with urllib.request.urlopen(self.url+'/api/export?workspace=own') as response:
            exported=json.load(response)
        self.assertEqual(exported['data'],fixture())
        self.assertEqual(Store(self.temp.name).load('own')['state'],fixture())

    def test_cancelled_state_is_saved_exported_and_reopened_over_http(self):
        state=fixture();state['tasks'][0]['status']='cancelled'
        self.post(dict(workspace='own',state=state,revision=0,operationId='cancelled'))
        with urllib.request.urlopen(self.url+'/api/export?workspace=own') as response:
            exported=json.load(response)
        self.assertEqual(exported['data'],state)
        state['tasks'][0]['status']='open'
        reopened=self.post(dict(workspace='own',state=state,revision=1,operationId='reopened'))
        self.assertEqual(reopened['state'],state)
    def test_cross_origin_writes_and_data_directory_access_are_rejected(self):
        with self.assertRaises(urllib.error.HTTPError) as ctx:self.post({},'https://unrelated.example')
        self.assertEqual(ctx.exception.code,403)
        with self.assertRaises(urllib.error.HTTPError) as ctx:urllib.request.urlopen(self.url+'/local-data/kontext.sqlite3')
        self.assertEqual(ctx.exception.code,404)
        self.assertEqual(self.server.store.load('own')['revision'],0)
    def test_validation_error_is_not_success(self):
        with self.assertRaises(urllib.error.HTTPError) as ctx:self.post(dict(workspace='own',state={},revision=0,operationId='bad'))
        self.assertEqual(ctx.exception.code,400)
        self.assertEqual(self.server.store.load('own')['revision'],0)

if __name__=='__main__':unittest.main()
