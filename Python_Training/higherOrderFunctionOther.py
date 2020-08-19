employeeDetails = {
    "name": "Mayank",
    "age": 20,
    "designation": "Manager",
    "salary": 20000
}


def incrementSalary(empObject, fn):
    fn(empObject)

def managerIncrement(empObject):
    empObject["salary"] *= 1.4

def developerIncrement(empObject):
    empObject["salary"] *= 1.2

if employeeDetails["designation"] == "Developer":
    incrementSalary(employeeDetails, developerIncrement)
else:
    incrementSalary(employeeDetails, managerIncrement)

print(employeeDetails["salary"])