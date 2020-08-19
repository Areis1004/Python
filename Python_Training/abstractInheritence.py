from abc import ABC, abstractmethod

class Employee(ABC):
    @abstractmethod
    def showName(self):
        pass

    def showDesignation(self):
        print("No designation Defined...")


class HrEmployee(Employee):

    def showName(self):
        print("My Name is HR Employee")

    def showSalary(self):
        print("The Salary is 30000")

class ExecutiveEmployee(Employee):
    def showName(self):
        print("The Name is Executive Employee")

    def showSalary(self):
        print("The salary is 40000")

    def showAge(self):
        print("The Age is 10")

    def showDesignation(self):
        print("I am a Executive Employee")


def showDetails(employee):
    employee.showName()


execEmployee = ExecutiveEmployee()
showDetails(execEmployee)
execEmployee.showDesignation()

hrEmployee = HrEmployee()
showDetails(hrEmployee)
hrEmployee.showDesignation()