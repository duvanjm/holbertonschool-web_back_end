export default function createEmployeesObject(departmentName, employees) {
  const empl = {
    [departmentName]: employees,
  };

  return empl;
}
