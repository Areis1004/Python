class Employee:

    def __init__(self, name, age, designation)
        self.name = name
        self.age = age
        self.designation = designation

employeeOne = Employee("Mayank", 10, "Designation")

class Manager(Employee):
    teamSize = 10


firstManager = Manager()

print(f"Emnployee Name is: {firstManager.name}")
print(f"Emnployee Age is: {firstManager.age}")
print(f"Emnployee Designation is: {firstManager.designation}")
print(f"Emnployee Team Size is: {firstManager.teamSize}")