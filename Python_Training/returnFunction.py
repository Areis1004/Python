def additionCalculator(initialValue):
    def addingOperation(addValue):
        return initialValue + addValue
    
    return addingOperation 

calculator = additionCalculator(10)
print(calculator(20))
print(calculator(100))