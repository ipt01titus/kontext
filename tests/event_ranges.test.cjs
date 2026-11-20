const test = require('node:test');
const assert = require('node:assert/strict');
require('../app/public/model.js');
const {eventEndDate, eventIsMultiDay, eventOccursOn, eventIsUpcoming} = globalThis.KontextModel;

test('existing events without an end date retain their single day', () => {
  const event = {date: '2026-11-20', start: '09:00', end: '10:00'};
  assert.equal(eventEndDate(event), '2026-11-20');
  assert.equal(eventIsMultiDay(event), false);
  assert.equal(eventOccursOn(event, '2026-11-20'), true);
  assert.equal(eventOccursOn(event, '2026-11-21'), false);
});

test('all-day ranges include both boundaries and the weekend', () => {
  const event = {date: '2026-11-20', endDate: '2026-11-23', start: '', end: ''};
  assert.deepEqual(['2026-11-19', '2026-11-20', '2026-11-21', '2026-11-22', '2026-11-23', '2026-11-24']
    .filter(day => eventOccursOn(event, day)), ['2026-11-20', '2026-11-21', '2026-11-22', '2026-11-23']);
});

test('an overnight event spans a year boundary with an earlier end clock time', () => {
  const event = {date: '2026-12-31', endDate: '2027-01-01', start: '20:00', end: '07:00'};
  assert.equal(eventIsMultiDay(event), true);
  assert.equal(eventOccursOn(event, '2026-12-31'), true);
  assert.equal(eventOccursOn(event, '2027-01-01'), true);
  assert.equal(eventOccursOn(event, '2027-01-02'), false);
});

test('a timed midnight end does not occupy the following day', () => {
  const event = {date: '2026-11-20', endDate: '2026-11-23', start: '10:00', end: '00:00'};
  assert.equal(eventOccursOn(event, '2026-11-22'), true);
  assert.equal(eventOccursOn(event, '2026-11-23'), false);
  assert.equal(eventIsUpcoming(event, '2026-11-23'), false);
});

test('an ongoing event remains in today and upcoming-person selections until its last day', () => {
  const event = {date: '2026-11-18', endDate: '2026-11-22', start: '10:00', end: '17:00'};
  assert.equal(eventIsUpcoming(event, '2026-11-17'), true);
  assert.equal(eventOccursOn(event, '2026-11-20'), true);
  assert.equal(eventIsUpcoming(event, '2026-11-22'), true);
  assert.equal(eventIsUpcoming(event, '2026-11-23'), false);
});
