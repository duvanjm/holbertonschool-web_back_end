const assert = require('assert');

const calculateNumber = require('./1-calcul');

describe('calculateNumber', () => {
  it('return Error', () => {
    assert.strictEqual(calculateNumber('DIVIDE', 1, 0), 'Error');
  });
  it('return correct value sum', () => {
    assert.strictEqual(calculateNumber('SUM', 1, 3), 4);
    assert.strictEqual(calculateNumber('SUM',1, 3.7), 5);
    assert.strictEqual(calculateNumber('SUM',1.2, 3.7), 5);
    assert.strictEqual(calculateNumber('SUM',1.5, 3.7), 6);
    assert.strictEqual(calculateNumber('SUM',-1.5, -3.7), -5);
    assert.strictEqual(calculateNumber('SUM',0.4, 0.5), 1);
  });
  it('return correct value sub', () => {
    assert.strictEqual(calculateNumber('SUBTRACT', 1.4, 4.5), -4);
    assert.strictEqual(calculateNumber('SUBTRACT', 1.2, 3.8), -3);
    assert.strictEqual(calculateNumber('SUBTRACT', -1, -3), 2);
    assert.strictEqual(calculateNumber('SUBTRACT', -1.4, -3.6), 3);
  });
  it('return correct value div', () => {
    assert.strictEqual(calculateNumber('DIVIDE', 1.4, 4.5), 0.2);
  });

});
