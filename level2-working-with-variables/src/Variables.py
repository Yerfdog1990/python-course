# 1. Declaration and Assignment
x = 10
y = 20
print(x + y)

# 2. Naming Variables
name1 = "Alex"
print(name1)
user_age = 5
print(user_age)
total_price = 100
print(total_price)

# 3. Dynamic Typing
age = "Alexander" # Store string
print(age)
age = 35 # Store integer
print(age)
age = "London" # Store string
print(age)
age = 3.14 # Store float
print(age)

# 4. Referential Nature of Variables
x = [1, 2, 3]
y = x

# Now both x and y refer to the same list.
# If the list changes using one variable, the other variable sees the change.

x.append(4)

print(y)

# Variable Naming Conventions:
# - Use lowercase letters and underscores to separate words.
# - Avoid using Python keywords as variable names.
# - Avoid using numbers as the first character of a variable name.

# 5. Variable Scope
# a) Local variables: Defined inside a function and accessible only within that function.

def my_function():
    x = 5
    print(x)

my_function()

# Here x exists only inside the function.

# b) Global variables: Defined outside functions and accessible throughout the program.

x = 10

def show_value():
    print(x)

show_value()

# Here x is a global variable.

# c) Non-local Variables: A non-local variable is used inside a nested (inner) function to refer to a variable defined in the outer function.

# Normally, if you assign a value to a variable inside a function, Python treats it as a local variable. To modify a variable from the enclosing function, you must use the nonlocal keyword.

def outer_function():
    count = 0   # variable in the outer function

    def inner_function():
        nonlocal count   # refer to the variable in outer_function
        count += 1
        print("Inner count:", count)

    inner_function()
    inner_function()
    print("Outer count:", count)

outer_function()

# 7. Immutability of Objects

text = "hello"
print(text)

text = text + " world" # This does not modify the original string; it creates a new one.
print(text)

# 8. Multiple Assignments
x, y, z = 1, 2, 3
print("x = ", x)
print("y = ", y)
print("z = ", z)

# Data Types
print(type(1)) # int
print(type(1.0)) # float
print(type("hello")) # str
print(type(True)) # bool
print(type([1, 2, 3])) # list
print(type({})) # dict
print(type(None)) # NoneType

# 9. Type Conversion
x = int("10")
print(x)
print(type(x)) # int

y = float("10.5")
print(y)
print(type(y)) # float

z = str(10)
print(z)
print(type(z)) # str

# 10. String Interpolation
name = "Alex"
print(f"Hello, {name}!")

# 11. Concatenation (joining strings)
name = "Alex"
age = 25
print("Hello, " + name + "! You are " + str(age) + " years old.")

# 12. Duplication
name = "Alex"
print(name * 3)