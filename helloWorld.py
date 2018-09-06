print("Hello World!!!")

print("This is my first python program")

intVal = 5
floatVal = 4.54

boolVal = True

print(boolVal)

boolVal = False

print(intVal)
print(floatVal)
print(boolVal)

# single line comment
"""
Saare jahaan se achha
"""
print("Adding above 2 numbers = ", intVal+floatVal)

operator1 = 2
operator2 = 2
operator3 = 2

operator1 **= 2
operator2 //= .5
operator3 %= 2
print(operator1, operator2, operator3)



# String slicing

string = "Alligator"

print(string[:4])

print(string[:3])
print(string[4:7])
print(string[6:])

print("-----------------------------------------\n")
string = "Manchester United"
print(string)
print("Length of the string is", len(string))
print(str(12345)[2])


str1 = "albania"
print("albania in upper case is ", str1.upper())

# print("albania in upper case is ", "albania".upper())

str2 = "BELGIUM"

print("BELGIUM in lower case is ", str2.lower())

# print("BELGIUM in lower case is ", "BELGIUM".lower())

print("\n-------------------Using print for concatenation------------------\n")

print("I am a string")
print(100)

city = "New Delhi"
country = "India"
population = 1000000

print("The capital of %s is %s" % (city, country))
print("The population of %s, the capital of %s is %d" % (city, country, population))


print("\n-------------------Ask user for input-----------\n")


city = input("Which city do you live in?")

print("You are a resident of %s" % city)


print("\n---------Evaluating comparison operators----------------\n")

print(8 > 8)
print(6 <= 7)
print(6 == 8)
print(6 != 7)

