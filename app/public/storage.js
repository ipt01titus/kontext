/* Disk persistence is acknowledged before the application reports a successful action. */
(function(){
"use strict";
const workspace=new URLSearchParams(location.search).get("workspace")==="demo"?"demo":"own";
const journalKey="kontext-mac-pending-"+workspace,recoveryKey="kontext-mac-recovered-"+workspace;
let revision=0,current=null,updatedAt=null;
const dialog=document.getElementById("save-dialog"),status=document.getElementById("save-state");
const clone=x=>structuredClone(x);
const esc=x=>String(x??"").replace(/[&<>"']/g,c=>({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"}[c]));
function label(text,error=false){status.textContent=text;status.classList.toggle("save-error",error);}
function received(result){revision=result.revision;current=result.state;updatedAt=result.updatedAt;label("Lokal gespeichert"+(updatedAt?" · "+new Date(updatedAt).toLocaleTimeString("de-DE",{hour:"2-digit",minute:"2-digit"}):""));return clone(current);}
function download(data,name){const url=URL.createObjectURL(new Blob([JSON.stringify(data,null,2)],{type:"application/json"})),a=document.createElement("a");a.href=url;a.download=name;a.click();setTimeout(()=>URL.revokeObjectURL(url),1000);}
function confirmChange(message){
 const el=document.getElementById("confirm-dialog");
 el.innerHTML=`<h2>Änderung bestätigen</h2><p>${esc(message)}</p><div class="save-actions"><button class="btn btn-secondary" id="cancel-change" autofocus>Abbrechen</button><button class="btn btn-primary" id="confirm-change">Bestätigen</button></div>`;
 el.showModal();
 return new Promise(resolve=>{const finish=value=>{el.oncancel=null;el.close();resolve(value);};el.oncancel=e=>{e.preventDefault();finish(false);};document.getElementById("cancel-change").onclick=()=>finish(false);document.getElementById("confirm-change").onclick=()=>finish(true);});
}
async function request(path,payload){
 const options={cache:"no-store",signal:AbortSignal.timeout(10000)};
 if(payload)Object.assign(options,{method:"POST",headers:{"Content-Type":"application/json","X-Kontext-Client":"1"},body:JSON.stringify(payload)});
 let response;
 try{response=await fetch(path,options);}catch{throw new Error("Der lokale Kontext-Dienst ist nicht erreichbar. Bitte den Starter erneut öffnen.");}
 const result=await response.json();
 if(!response.ok){const error=new Error(result.error||"Der lokale Dienst antwortet nicht.");error.status=response.status;throw error;}
 return result;
}
function remember(operation){try{localStorage.setItem(journalKey,JSON.stringify(operation));}catch{}}
function readJournal(){try{return JSON.parse(localStorage.getItem(journalKey)||"null");}catch{return null;}}
function forget(){try{localStorage.removeItem(journalKey);}catch{}}
async function interrupted(error,operation){
 label(error.status===409?"Konflikt · Eingaben erhalten":"Noch nicht gespeichert",true);
 dialog.innerHTML=`<h2>${error.status===409?"Ein anderer Stand wurde gespeichert":"Speichern ist unterbrochen"}</h2><p>${esc(error.message)}</p><p>Deine Eingaben bleiben in diesem Fenster erhalten. Öffne bei Bedarf den Kontext-Starter erneut und versuche es noch einmal.</p><div class="save-actions">${error.status!==409?'<button class="btn btn-primary" id="retry-save">Erneut versuchen</button>':""}<button class="btn btn-secondary" id="download-pending">Eingaben herunterladen</button><button class="btn btn-secondary" id="reload-saved">Gespeicherten Stand laden</button></div>`;
 if(!dialog.open)dialog.showModal();
 return new Promise(resolve=>{
  document.getElementById("retry-save")?.addEventListener("click",()=>resolve());
  document.getElementById("download-pending").onclick=()=>download(operation.payload?.state||operation,"kontext-ungespeicherte-eingaben.json");
  document.getElementById("reload-saved").onclick=async()=>{
   if(!await confirmChange("Den zuletzt gespeicherten Stand laden? Die ungespeicherte Fassung bleibt zusätzlich als gerettete Eingabe in diesem Browser erhalten."))return;
   try{const old=JSON.parse(localStorage.getItem(recoveryKey)||"[]");old.push({at:new Date().toISOString(),operation});localStorage.setItem(recoveryKey,JSON.stringify(old));}
   catch{download(operation.payload?.state||operation,"kontext-ungespeicherte-eingaben.json");}
   forget();location.reload();
  };
 });
}
async function commit(operation){
 remember(operation);
 dialog.innerHTML='<h2>Wird lokal gespeichert …</h2><p>Bitte kurz warten.</p>';
 if(!dialog.open)dialog.showModal();label("Wird gespeichert …");
 for(;;){
  try{const result=await request(operation.path,operation.payload);forget();dialog.close();return received(result);}
  catch(error){
   if(error.status===400||error.status===413){forget();dialog.close();label("Nicht gespeichert · Eingabe prüfen",true);throw error;}
   await interrupted(error,operation);
  }
 }
}
dialog.addEventListener("cancel",e=>e.preventDefault());
async function load(factory){
 for(;;){
  try{
   const result=await request("/api/state?workspace="+workspace);received(result);
   const pending=readJournal();
   if(pending?.payload?.workspace===workspace)return await commit(pending);
   if(!current)return await save(factory());
   return clone(current);
  }catch(error){
   if(error.status===400){label(error.message,true);throw error;}
   await interrupted(error,readJournal()||{path:"/api/state?workspace="+workspace});
  }
 }
}
function save(state,path="/api/state",extra={}){return commit({path,payload:{workspace,revision,operationId:crypto.randomUUID(),state:clone(state),...extra}});}
function prepareImport(raw){
 const state=clone(raw?.format==="kontext-export-v1"?raw.data:raw);
 if(!state||state.schema!==1||!Object.values(KontextModel.collections).every(k=>Array.isArray(state[k])))throw new Error("Diese Datei enthält keinen unterstützten Kontext-Datenbestand.");
 const seen=new Set();
 for(const x of Object.values(KontextModel.collections).flatMap(k=>state[k]))if(x.number!==undefined){if(!Number.isSafeInteger(x.number)||x.number<1||seen.has(x.number))throw new Error("Die Datei enthält ungültige oder doppelte Eintragsnummern. Es wurde nichts übernommen.");seen.add(x.number);}
 KontextModel.migrate(state);
 state.projects.forEach(p=>p.color||= "#6b9182");
 state.nextNumber=Math.max(state.nextNumber,current?.nextNumber||1);
 return state;
}
async function panel(){
 const el=document.getElementById("data-dialog");
 const result=await request("/api/backups?workspace="+workspace);
 const recovered=(()=>{try{return JSON.parse(localStorage.getItem(recoveryKey)||"[]");}catch{return [];}})();
 const legacy=(()=>{try{return localStorage.getItem("kontext-entwurf-v1");}catch{return null;}})();
 el.innerHTML=`<div class="modal-header"><h2>Daten & Sicherungen</h2><button class="icon-button" id="close-data" aria-label="Schließen">×</button></div><div class="modal-body"><p>Arbeitsbereich: <strong>${workspace==="own"?"Eigene Daten":"Beispieldaten"}</strong>. Vor jeder Änderung eines vorhandenen Bestands wird automatisch eine Sicherung erstellt.</p><div class="data-buttons"><a class="btn btn-primary" href="/api/export?workspace=${workspace}">Daten exportieren</a><button class="btn btn-secondary" id="backup-now">Jetzt sichern</button></div><h3>Datei übernehmen</h3><p>Ein Kontext-Export oder ein früherer Entwurfsbestand kann diesen Bereich ersetzen. Der aktuelle Stand wird vorher gesichert.</p><label class="btn btn-secondary">JSON-Datei auswählen<input id="import-file" type="file" accept=".json,application/json" hidden></label>${legacy?'<button class="btn btn-secondary" id="import-legacy">Entwurf aus diesem Browser übernehmen</button>':""}<h3>Sicherung wiederherstellen</h3><p>Es wird nur der gewählte Arbeitsbereich zurückgesetzt. Vorher entsteht eine weitere Sicherung des aktuellen Stands.</p><select id="restore-choice" aria-label="Sicherung auswählen"><option value="">Sicherung auswählen</option>${result.backups.map(b=>`<option value="${esc(b.name)}">${esc(new Date(b.at).toLocaleString("de-DE"))} · ${Math.ceil(b.size/1024)} KB</option>`).join("")}</select><button class="btn btn-secondary" id="restore-backup">Wiederherstellen</button>${recovered.length?'<h3>Gerettete Eingaben</h3><button class="btn btn-secondary" id="download-recovered">Gerettete Eingaben herunterladen</button>':""}<p id="data-message" role="status"></p><p class="secondary">Kontext 0.2.0 · Lokal auf diesem Mac. Geräteabgleich und externe Konten sind noch nicht angebunden. Automatische Sicherungen bleiben im Datenordner erhalten.</p></div>`;
 if(!el.open)el.showModal();document.getElementById("close-data").onclick=()=>el.close();
 function failure(error){document.getElementById("data-message").textContent=error.message;}
 document.getElementById("backup-now").onclick=async()=>{try{await request("/api/backup",{});await panel();document.getElementById("data-message").textContent="Sicherung erstellt.";}catch(e){failure(e);}};
 async function importData(raw){try{const state=prepareImport(raw);if(!await confirmChange("Diesen Arbeitsbereich durch die Datei ersetzen? Der aktuelle Stand wird vorher gesichert."))return;await save(state,"/api/import");location.reload();}catch(e){failure(e);}}
 document.getElementById("import-file").onchange=async e=>{try{const file=e.target.files[0];if(file){if(file.size>10*1024*1024)throw new Error("Die Datei ist größer als 10 MB.");await importData(JSON.parse(await file.text()));}}catch(error){failure(error);}};
 document.getElementById("import-legacy")?.addEventListener("click",()=>importData(JSON.parse(legacy)));
 document.getElementById("restore-backup").onclick=async()=>{const name=document.getElementById("restore-choice").value;if(!name){failure(new Error("Wähle zuerst eine Sicherung."));return;}if(!await confirmChange("Diesen Arbeitsbereich aus der Sicherung wiederherstellen? Der aktuelle Stand wird vorher gesichert."))return;try{await commit({path:"/api/restore",payload:{workspace,name,revision,operationId:crypto.randomUUID()}});location.reload();}catch(e){failure(e);}};
 document.getElementById("download-recovered")?.addEventListener("click",()=>download(recovered,"kontext-gerettete-eingaben.json"));
}
document.getElementById("workspace-label").textContent=workspace==="own"?"Eigene Daten":"Beispieldaten";
document.getElementById("workspace-own").setAttribute("aria-current",workspace==="own"?"page":"false");
document.getElementById("workspace-demo").setAttribute("aria-current",workspace==="demo"?"page":"false");
document.getElementById("open-data").onclick=()=>panel().catch(e=>label(e.message,true));
window.addEventListener("beforeunload",event=>{if(readJournal()){event.preventDefault();event.returnValue="";}});
window.KontextStorage={workspace,load,save,confirmChange,get currentState(){return clone(current);}};
})();
