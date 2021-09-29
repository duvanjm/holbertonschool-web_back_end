const calculateNumber = require("./2-calcul_chai.js");
const { expect } = require('chai');

describe('calculateNumber', () => {
    it('returns rounded sum with SUM', () => {
    expect(calculateNumber('SUM', 1, 3)).to.equal(4);
    expect(calculateNumber('SUM', 1.6, 3)).to.equal(5);
    expect(calculateNumber('SUM', 1.2, 3.8)).to.equal(5);
    expect(calculateNumber('SUM', -1, -3)).to.equal(-4);
    expect(calculateNumber('SUM',-1.4, -3.6)).to.equal(-5);
    });
    it('returns rounded sum with SUBTRACT', () => {
        expect(calculateNumber('SUBTRACT',1, 3)).to.equal(-2);
        expect(calculateNumber('SUBTRACT', 1.6, 3)).to.equal(-1);
        expect(calculateNumber('SUBTRACT', 1.2, 3.8)).to.equal(-3);
        expect(calculateNumber('SUBTRACT', -1, -3)).to.equal(2);
        expect(calculateNumber('SUBTRACT',-1.4, -3.6)).to.equal(3);
    });
    it('returns rounded sum with DIVIDE', () => {
        expect(calculateNumber('DIVIDE', 1.4, 4.5)).to.equal(0.2);
    });
    it('returns error string when DIVIDE by 0', () => {
        expect(calculateNumber('DIVIDE', 1.4, 0)).to.equal('Error');
    });
    it('should throw error if NaN passed', function () {
        expect(() => calculateNumber('SUM', NaN, 3)).to.throw();
    });
    it('should throw error if invalid type', function () {
        expect(() => calculateNumber('blah', 2, 3)).to.throw();
    });
});
