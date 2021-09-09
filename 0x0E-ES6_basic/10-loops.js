export default function appendToEachArrayValue(array, appendString) {
  const n_array = [];
  for (const idx of array) {
    n_array.push(appendString + idx);
  }

  return array;
}
