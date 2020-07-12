class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary * 1.1

    def incrementSalary(self):
        self.salary = self.salary * 1.1

    def incrementAge(self, incrementStep):
        self.age = self.age + incrementStep

employeeList = []

print(type(employeeList))

print(len(employeeList))

employeeList.append(Employee("Mayank", 20, 100))
employeeList.append(Employee("Ankit", 30, 120))
employeeList.append(Employee("Aniket", 40, 140))

print(type(employeeList))

print(len(employeeList))

for emp in employeeList:
    emp.incrementSalary()
    emp.incrementAge(2)
    print(f"Employee Salary is : {emp.salary}")
    print(f"Incremented Age is {emp.age}")