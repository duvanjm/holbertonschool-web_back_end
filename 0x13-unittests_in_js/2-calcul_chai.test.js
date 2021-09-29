const assert = require('assert');

const expect = require('chai').expect;

const calculateNumber = require('./1-calcul');

describe('calculateNumber', () => {
  it('return Error', () => {
    expect(calculateNumber('DIVIDE', 1, 0)).to.equal('Error');
  });
  it('return correct value sum', () => {
    expect(calculateNumber('SUM', 1.4, 4.5)).to.equal(6);
  });
  it('return correct value sub', () => {
    expect(calculateNumber('SUBTRACT', 1.4, 4.5)).to.equal(-4);
  });
  it('return correct value div', () => {
    expect(calculateNumber('DIVIDE', 1.4, 4.5)).to.equal(0.2);
  });
});
