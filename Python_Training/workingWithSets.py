fruits = { "Apple", "Oranges", "Cherry", "Banana" } 

print(fruits)

fruits.add("WaterMelons")
fruits.add("WaterMelons")

print(fruits)

valueList = [1, 2, 3, 4, 1, 2, 5, 6]

distintValue = set({})
for val in valueList:
    distintValue.add(val)

print(distintValue)

print( 10 in distintValue)

setData = {"1", 2, "3", 3, "3", 1}
print(setData)

print(f"Length of the Set is: {len(setData)}")

setData.remove("1")

print(setData)

del setData

employeesName = {"Mayank", "Rahul", "Ankit"}
employeesName.pop()

employeesName.add("Other NAme")

print(employeesName)

employeesName.clear()

print(employeesName)

print(type(employeesName))

setOne = {1, 2, 3}
setTwo = {3, 4, 5}

setThree = setOne.union(setTwo)

print(setThree)

myTuple = ("A", "B", "C")
print(type(myTuple))

mySet = set(myTuple)
print(mySet)
print(type(mySet))

mySet.add("D")
print(mySet)

myTuple = tuple(mySet)
print(myTuple)

myTuple = (1, 2, 3)
myTuple = (3, 4, 5)

print(myTuple)

listData = [1, 2, 3, 4, 12, 4, 1]
myDataSet = set(listData)

print(myDataSet)
print(myDataSet)

parentSet = {1, 2, 3, 4}
childSet = {1, 3}

print(parentSet.issubset(childSet))
