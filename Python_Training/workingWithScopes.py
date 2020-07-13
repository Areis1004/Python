# Global Variable "name"
name = "Ankit"

def scopingData():
    # Same Global Variable Accessed
    global name
    name = "Anshul"
    print(f"User Name is: {name}")
    print(f"User Name is: {name}")

#scopingData()
#print(f"User Name is: {name}")

otherData = 10

def outerFunction():
    outerName = "Mayank"
    print(outerName)
    innerName = "Ankit Gupta"
    
    def innerFunction():
        print(outerName)
        print(otherData)
        innerName = "Ankit"

        def otherFunction():
            print(innerName)
            print(otherData)

        otherFunction()

    innerFunction()

outerFunction()
