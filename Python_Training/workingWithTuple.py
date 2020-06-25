sampleTuple = (1, 2, 3, 4)

print(type(sampleTuple))

stringOutput = f"The value at Index One is: {sampleTuple[1]}, the value at index Three is {sampleTuple[3]}"

print(stringOutput)

hetrogeneousTuple = (1, 1.2, "Random", True, None)

print(f"Data from the Hetrogenious Tuple {hetrogeneousTuple[2]}")

print(f"Length of the Tuple: {len(hetrogeneousTuple)}")

for items in hetrogeneousTuple:
    print(items)
    print("Hello")

innerTuples = ((1, 2), (1, 2, 3), (1, 2, 3, 4), "Random Data", 100)
print(innerTuples[4])

singleTuple = ("Hello All",)
print(singleTuple[0])
print(type(singleTuple))

complexTuple = (1, (2, (3, 4, (5, 6))))
(a, (b)) = complexTuple
print(a)

a, b = b, a

integerTuple = (1, 2, 3, 4, 5)
print(f"Is Value Found: {6 in integerTuple}")

print(integerTuple[-1])

print(integerTuple[1:4])

newTuple = integerTuple[:]
print(newTuple)

print(newTuple == integerTuple)

print(newTuple is integerTuple)

aa = (1, 2, 3)
bb = (1, 2, 3)

print(aa == bb)

print(aa is bb)

stringTuple = tuple("Hello")

print(stringTuple)

del stringTuple


first = (1, 2, 3)
second = (4, 5, 6)
third = first + second
print(third)