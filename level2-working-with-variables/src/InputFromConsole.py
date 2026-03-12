# The input() Function
name = input("Enter your name: ")
print("Hello", name)

# Using input() Without a Prompt
name = input()
print("Hello", name)

# Example: Multiple Inputs
name = input("Enter your name: ")
city = input("Enter your city: ")

print("Hello", name)
print("You live in", city)

# Entering Numbers from the Console
age = int(input("Enter your age: "))
print(f"You are {age} years old.")

# Converting Input to an Integer
age = input("Enter your age: ")
age = int(age)

print("In 10 years you will be", age + 10)

# Shorter Version (Single Line)
age = int(input("Enter your age: "))
print("In 10 years you will be", age + 10)

# Converting Input to a Floating Point Number
price = float(input("Enter the product price: "))
print("The price with tax is", price * 1.1)