/* eslint-disable no-restricted-syntax */
export default function appendToEachArrayValue(array, appendString) {
  const nArray = [];
  for (const idx of array) {
    nArray.push(appendString + idx);
  }

  return array;
}
