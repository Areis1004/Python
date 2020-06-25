salutation = "Hello World..."

advancedSalutation = """Hello World
Welcome to Python
This is Introductory Session"""

advancedNewLineString = "Hello World \nWelcome to Python\nThis is Introductory Session"

print(advancedNewLineString)
print(advancedSalutation)

name = "Random"
print(name[2])

print("z" in name)

stripData = "  Removing WhiteSpaces...   "
print(stripData)
print(stripData.strip())

data = "hello"
print(data.replace("h", "H"))

print(len(data)) 

userInfo = "Random, Name Update"
otherdata = userInfo.split("Na")
print(otherdata)

print(userInfo.upper())
print(userInfo.lower())

print("random".capitalize() == "Random")

print(type(otherdata))

name = "Random Name"
age = 20

print("Hello " + name + ", your age is: " + str(age))

d = "Hi, {0}, your age is: {1}".format(name.upper(), age + 10)

d = "Hello " + name + ", your age is: " + str(age)

print(d)