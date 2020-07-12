def employeeSalutation(name):
    print(f"Hello {name}...")

#employeeSalutation("Mayank")
#employeeSalutation("Ankit")
#employeeSalutation("Anshul")

def additionFunction(first, second):
    return first + second

#print(additionFunction(1, 3))
#print(additionFunction(1, 11))
#print(additionFunction(11, 11))
#print(additionFunction("Hello ", "World..."))
#print(additionFunction(1.1, 11.9))

def additionFunctionOther(tuppleInput):
    addition = 0
    for val in tuppleInput:
        addition += val
    print(addition)


#additionFunctionOther([1, 2, 3, 4])

def additionFunctionSimple(*inputValues):
    addition = 0
    for val in inputValues:
        addition += val
    print(f"The Addition of Numbers would be: {addition}")

#additionFunctionSimple(1, 2, 3, 4)

def employeeData(name, age, designation):
    print(f"The Name is {name}")

#employeeData(designation = "Developer", age = 10, name = "Mayank")

def anonymousInputFunction(**details):
    print(type(details))
    print(details["name"])
    for key, value in details.items():
        print(f"Employee {key} is {value}")


#anonymousInputFunction(age = 20, name = "mayank")

def forcedValues(name = "Mayank", age = 200, designation = "None"):
    print(f"The User Name is: {name}")

#forcedValues(name = "Anshul")

def getData(data):
    print(data)

getData([1, 2, 3, 4])
getData((1, 2, 3, 4))
getData({
    "name": "Mayank",
    "age": 20
})
getData(10)
getData("Mayank")