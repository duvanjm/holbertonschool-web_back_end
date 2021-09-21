export default function updateUniqueItems(map) {
  if (map instanceof Map === false) {
    throw new Error('Cannot process');
  }

  for (const [key, val] of map) {
    if (val === 1) {
      map.set(key, 100);
    }
  }
}
