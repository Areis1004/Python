employee = {
    "name": "Mayank",
    "age": 20,
    "designation": "Developer",
    "salary": 10
}

print(type(employee))

print(f"Employee age is {employee.get('age')}")

employee["age"] = 30

print("Employee age is " + str(employee["age"]))

for key in employee:
    print(f"Employee {key} is {employee[key]}")

for key in employee.values():
    print(f"Employee values: {key}")

for key, value in employee.items():
    print(f"Employee {key} is {value}")

print(len(employee))

if "salary" in employee:
    print("Salary Key is Available...")

employee["bonus"] = 20

if "bonus" in employee:
    print("Bonus Key is Available...")

del employee["bonus"]

print(len(employee))

print(len(employee))

myDict = employee.copy()

print(myDict)

myDict["name"] = "Anshul"

print(employee["name"])

myOtherDict = myDict
myOtherDict["age"] = 100

print(myDict["age"])

sample = dict(employee)
print(sample)

newEmployee = {
    "name": "Ankit",
    "age": 40,
    "designation": "Developer",
    "address": {
        "street": "1A Prashant Vihar",
        "city": "Delhi",
        "state": "Delhi"
    }
}

print(newEmployee)