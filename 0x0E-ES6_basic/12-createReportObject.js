export default function createReportObject(employeesList) {
  const emplo = {
    allEmployees: employeesList,
    getNumberOfDepartments: (i) => Object.keys(i).length,
  };

  return emplo;
}
