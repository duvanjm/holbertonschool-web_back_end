export default function getStudentIdsSum(lst) {
  const numbers = lst.map((x) => x.id);
  const reducer = (prev, current) => prev + current;

  return numbers.reduce(reducer);
}
