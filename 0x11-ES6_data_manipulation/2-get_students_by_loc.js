export default function getStudentsByLocation(lst, city) {
  return lst.filter((l) => l.location === city);
}
