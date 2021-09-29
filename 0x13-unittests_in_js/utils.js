const Utils = {
  calculateNumber(type, a, b) {
    if (type === 'SUM') {
      return Math.round(a) + Math.round(b);
    } if (type === 'SUBTRACT') {
      return Math.round(a) - Math.round(b);
    } if (type === 'DIVIDE') {
      if (b === 0) {
        return ('Error');
      } else {
        return Math.round(a) / Math.round(b);
      }
    }
  }
}

module.exports = Utils;
