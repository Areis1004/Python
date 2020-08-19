inputNumberData = [10, 2, 40, 30, 100, 400, 300, 50, 20]

def search_linear(inputList, search_value):
    numberFound = "Not Found"
    for data in inputList:
        if data == search_value:
            numberFound = "Found"
            break
    print(f"The number is {numberFound}")

search_linear(inputNumberData, 80)
search_linear(inputNumberData, 50)