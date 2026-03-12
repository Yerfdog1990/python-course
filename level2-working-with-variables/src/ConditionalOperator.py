# if else
y = 4

if y > 5:
    print("y is greater than 5")
else:
    print("y is not greater than 5")

#Examples with user input
age = int(input("Enter your age: "))

if age >= 18:
    print("you are an adult")
else:
    print("go do your homework")

# if Without else
age = int(input("Enter your age: "))

if age >= 21:
    print("Here's your beer!")

# if elif else

#  1. Nested if version
x, y = 5, -8

if x > 0 and y > 0:
    print("first quadrant")
else:
    if x < 0 and y > 0:
        print("second quadrant")
    else:
        if x < 0 and y < 0:
            print("third quadrant")
        else:
            print("fourth quadrant")

# 2. Nested if-else version
x, y = 5, -8

if x > 0 and y > 0:
    print("first quadrant")
elif x < 0 and y > 0:
    print("second quadrant")
elif x < 0 and y < 0:
    print("third quadrant")
else:
    print("fourth quadrant")


# Ternary Operator
x = 5
print("x is greater than 5" if x > 5 else "x is less than or equal to 5")