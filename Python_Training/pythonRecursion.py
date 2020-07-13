
def factorial(inputValue):

    if inputValue > 0:
        if inputValue == 1: 
            return 1
        else:
            return inputValue * factorial(inputValue - 1)
    else:
        raise Exception("Provide Positive Numbers")

print(factorial(3))