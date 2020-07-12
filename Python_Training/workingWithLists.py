fruitList = ["Apple", "Banana", "Oranges", "Cherry"]

print(fruitList)

print(type(fruitList))

print(fruitList[2])

print(fruitList[-3])

print(fruitList[:])

print(fruitList[1:-2])

originalList = [1, 2, 3]

copyList = originalList

copyList[0] = 10

copyList[1] = 20

print(copyList)
print(originalList)

print(copyList is originalList)

copyByValue = originalList[:]

copyByValue[0] = 1000

print(copyByValue)
print(originalList)

print(copyByValue is originalList)

otherCopyByValue = list(originalList)


otherCopyByValue[0] = 1000

print(otherCopyByValue)
print(originalList)

print(copyByValue is originalList)

listOfLists = [[1, 2], [3, 4], [4, 5]]
copyOfListOfLists = listOfLists[:]

print(f"Value is: {listOfLists is copyOfListOfLists}")

copyOfListOfLists[0][1] = 2000
copyOfListOfLists[0][0] = 1000

print(listOfLists[0] is copyOfListOfLists[0])
print(listOfLists)


sampleList = [[1, 2, 3]]
anotherSample = sampleList * 10
anotherSample[0].append(4)

print(anotherSample)
print(anotherSample[0] is anotherSample[1])

print([1, 2, 3, 2, 2].count(2))

print(30 in [1, 2, 3, 4])


a = [1, 2, 3, 2]
a.remove(3)

a.insert(2, 2000)
print(a)

a = [1, 2]
b = [2, 3]
c = a + b
print(c)







