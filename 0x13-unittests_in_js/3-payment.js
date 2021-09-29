const utils = require('./utils');

function sendPaymentRequestToApi(totalAmount, totalShipping) {
  const sum = utils.calculateNumber('SUM', totalAmount, totalShipping);
  console.log(`The total is: ${sum}`);
  return sum;
}

module.exports = sendPaymentRequestToApi;
