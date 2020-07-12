def addition(x, y):
    return x + y

output = addition(1, 2)

additionFunction = lambda x, y : x + y

output = additionFunction(10, 200)

multiplication = lambda *a : type(a)

output = multiplication(10, 200)

randomAdditionThreeParam = lambda a, b, c : a + b + c

print(f"The output from the Function is {multiplication(1, 2, 3)} ")