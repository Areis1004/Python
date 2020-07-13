import sys

def rangeEstimator(range):
    if range < 100 and range > 0:
        print(f"Valid Range: {range}")
    elif range > 100 or range < 0:
        raise Exception(f"Invalid Range: {range}")

def mainFunction():
    try:
        rangeEstimator(150)
    except:
        err = sys.exc_info()[1].args[0]
        print(err)
    else:
        print("Function Executed Sucessfully")
    
mainFunction()

print("Done")