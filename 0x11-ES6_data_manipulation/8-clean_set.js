export default function cleanSet(set, startString) {
  if (typeof set !== 'object' || startString.length === 0) {
    return '';
  }

  const str = [];
  for (const element of set) {
    if (element && element.startsWith(startString)) {
      str.push(element.slice(startString.length));
    }
  }
  return str.join('-');
}
