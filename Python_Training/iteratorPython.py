def myFunc():
    yield 10
    yield 209
    yield 301

def customRange(inputValue):
    returnVariable = -1
    while returnVariable < inputValue - 1:
        returnVariable += 1
        yield(returnVariable)


iteratorObject = customRange(10)

print(next(iteratorObject))
print(next(iteratorObject))
print(next(iteratorObject))
