const calculateNumber = require("./1-calcul.js");
const mocha = require('mocha');
const assert = require("assert");

describe('calculateNumber', () => {
    it('returns rounded sum with SUM', () => {
    assert.strictEqual(calculateNumber('SUM', 1, 3), 4);
    assert.strictEqual(calculateNumber('SUM', 1.6, 3), 5);
    assert.strictEqual(calculateNumber('SUM', 1.2, 3.8), 5);
    assert.strictEqual(calculateNumber('SUM', -1, -3), -4);
    assert.strictEqual(calculateNumber('SUM',-1.4, -3.6), -5);
    });
    it('returns rounded sum with SUBTRACT', () => {
        assert.strictEqual(calculateNumber('SUBTRACT', 1, 3), -2);
        assert.strictEqual(calculateNumber('SUBTRACT', 1.6, 3), -1);
        assert.strictEqual(calculateNumber('SUBTRACT', 1.2, 3.8), -3);
        assert.strictEqual(calculateNumber('SUBTRACT', -1, -3), 2);
        assert.strictEqual(calculateNumber('SUBTRACT',-1.4, -3.6), 3);
    });
    it('returns rounded sum with DIVIDE', () => {
        assert.strictEqual(calculateNumber('DIVIDE', 1.4, 4.5), 0.2);
    });
    it('returns error string when DIVIDE by 0', () => {
        assert.strictEqual(calculateNumber('DIVIDE', 1.4, 0), 'Error');
    });
    it('should throw error if NaN passed', function () {
        assert.throws(() => calculateNumber('SUM', NaN, 3), '[Function: TypeError]');
    });
    it('should throw error if invalid type', function () {
        assert.throws(() => calculateNumber('blah', 2, 3), '[Function: TypeError]');
    });
});
