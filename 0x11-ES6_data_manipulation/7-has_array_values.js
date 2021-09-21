export default function hasValuesFromArray(set, array) {
  for (const elemet of array) {
    if (set.has(elemet) === false) {
      return false;
    }
  }
  return true;
}
