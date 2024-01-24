export default function createEmployeesObject(departmentName, employees) {
    const newDict = {
        [departmentName]: employees,
    };
    return newDict;
}