const { expect, assert } = require('chai');
const sinon = require('sinon');
const { spy, stub } = require('sinon');

const sendPaymentRequestToApi = require('./4-payment');
const utils = require('./utils');

describe('sendPaymentRequestToApi', () => {
    it('should call Util.calculateNumber', () => {
        const functionStub = sinon.stub(utils, 'calculateNumber');
        functionStub.returns(10);
        
        const consoleSpy = sinon.spy(console, 'log');

        const apiRequest = sendPaymentRequestToApi(100, 20);

        expect(functionStub.calledOnceWithExactly('SUM', 100, 20)).to.equal(true);
        expect (consoleSpy.calledWithExactly('The total is: 10'));
        expect(utils.calculateNumber('SUM', 100, 20)).to.equal(apiRequest);

        functionStub.restore();
        consoleSpy.restore();
    });
});
