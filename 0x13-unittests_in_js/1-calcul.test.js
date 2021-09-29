const assert = require('assert');

const calculateNumber = require('./1-calcul');

describe('calculateNumber', () => {
  it('return Error', () => {
    assert.equal(calculateNumber('DIVIDE', 1, 0), 'Error');
  });
  it('return correct value sum', () => {
    assert.equal(calculateNumber('SUM', 1.4, 4.5), 6);
  });
  it('return correct value sub', () => {
    assert.equal(calculateNumber('SUBTRACT', 1.4, 4.5), -4);
  });
  it('return correct value div', () => {
    assert.equal(calculateNumber('DIVIDE', 1.4, 4.5), 0.2);
  });
  
});
