# Converting a String to an Integer
num_str = "42"
num_int = int(num_str)
print(num_int)  # Output: 42

# Error When the String Is Not a Number
num_str = "forty two"
#num_int = int(num_str)
#print(num_int)  # ValueError: invalid literal for int() with base 10: 'forty two'

# Converting a Floating-Point Number to an Integer
num_float = 42.9
num_int = int(num_float)
print(num_int)  # Output: 42

# Converting Boolean Values to Integers
true_bool = True
false_bool = False

print(int(true_bool))   # Output: 1
print(int(false_bool))  # Output: 0

# Converting an Integer to a String
num_int = 42
num_str = str(num_int)

print(num_str)  # Output: "42"

# Converting a Floating-Point Number to a String
num_float = 42.9
num_str = str(num_float)

print(num_str)  # Output: "42.9"

# Converting Boolean Values to Strings
true_bool = True
false_bool = False

print(str(true_bool))   # Output: "True"
print(str(false_bool))  # Output: "False"

# Converting a String to a Floating-Point Number
num_str = "42.9"
num_float = float(num_str)

print(num_float)  # Output: 42.9

# Converting an Integer to a Floating-Point Number
num_int = 42
num_float = float(num_int)

print(num_float)  # Output: 42.0

# Converting Boolean Values to Floating-Point Numbers
true_bool = True
false_bool = False

print(float(true_bool))   # Output: 1.0
print(float(false_bool))  # Output: 0.0