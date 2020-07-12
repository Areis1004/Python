class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age


    
employeeOne = Employee("Mayank", 10)
employeeTwo = Employee("Ankit", 20)

employeeOne.salary = 100
employeeOne.designation = "Developer"

print(f"Name of the Employee is: {employeeOne.name}")
print(f"Age of the Employee is: {employeeOne.age}")

print(f"Name of the Employee is: {employeeTwo.name}")
print(f"Age of the Employee is: {employeeTwo.age}")

# del Employee.name

# employeeOne.name = "Ankit"

print(employeeTwo.name)
#print(employeeOne.name)

print(employeeOne is employeeTwo)