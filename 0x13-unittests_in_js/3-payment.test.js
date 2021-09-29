const expect = require('chai').expect;

const sinon = require('sinon');

const { spy } = require('sinon');

const sendPaymentRequestToApi = require('./3-payment');
const utils = require('./utils');

describe('sendPaymentRequestToApi', () => {
  it('call util.calculate number', () => {
    const spy = sinon.spy(utils, 'calculateNumber');
    const spyConsole = sinon.spy(console, 'log');
    const sendapi = sendPaymentRequestToApi(100, 20);

    expect(spy.calledOnceWithExactly('SUM', 100, 20)).to.equal(true);
    expect(spyConsole.calledWithExactly('The total is: 120')).to.equal(true);
    expect(utils.calculateNumber('SUM', 100, 20)).to.equal(sendapi);
  
    spy.restore();
    spyConsole.restore();
  });
});
