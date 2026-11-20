const test = require('node:test');
const assert = require('node:assert/strict');
require('../app/public/model.js');
const {isTaskOpen, isTaskBlocked, migrate} = globalThis.KontextModel;

test('cancelled activities leave open-work selections while remaining distinct from completed work', () => {
  const tasks = ['open', 'progress', 'done', 'cancelled'].map((status, i) => ({id: String(i), status}));
  assert.deepEqual(tasks.filter(isTaskOpen).map(t => t.status), ['open', 'progress']);
  assert.equal(tasks[3].status, 'cancelled');
});

test('a cancelled prerequisite remains unmet and retains the successor relationship', () => {
  const predecessor = {id: 'before', status: 'cancelled'};
  const successor = {id: 'after', status: 'open', predecessors: ['before']};
  assert.equal(isTaskBlocked([predecessor, successor], successor), true);
  predecessor.status = 'done';
  assert.equal(isTaskBlocked([predecessor, successor], successor), false);
  predecessor.status = 'open';
  assert.equal(isTaskBlocked([predecessor, successor], successor), true);
  assert.deepEqual(successor.predecessors, ['before']);
});

test('loading a cancelled activity preserves its identity, number, comments and links', () => {
  const state = {schema: 1, hierarchyVersion: 1, nextNumber: 8, projects: [], people: [], objects: [], goals: [], events: [],
    tasks: [{id: 'task', number: 7, name: 'Nicht mehr relevant', status: 'cancelled', projects: [],
      steps: [{text: 'Erhalten', done: false}], comments: [{text: 'Kontext erhalten'}], predecessors: ['before']}]};
  assert.deepEqual(migrate(structuredClone(state)), state);
});
