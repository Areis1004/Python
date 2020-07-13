try:
    x =1
    print(x/1)
except NameError:
    print("Completed With Errors...")
except ZeroDivisionError:
    print("Zero Division Error")
except:
    print("Generic Error")
else:
    print("Executed Without any Errors...")
finally:
    print("This is the Final Block")

print("Done")