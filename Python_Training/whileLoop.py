
employeeCount = [{
    "name": "Ankit",
    "age": 40
}, {
    "name": "Anshul",
    "age": 50
}, {
    "name": "Mayank",
    "age": 40
}]

for emp in employeeCount:
    if emp["age"] < 45:
        break
    print(f"Employee Name with Age less than 45 is: {emp['name']}")

count = 0
while count < len(employeeCount):
    if employeeCount[count]["age"] > 45:
        count += 1
        continue
    print(employeeCount[count]["name"])
    count += 1
    