# Example 1: String Concatenation
name = "Alex" + "Alex"
print(name)

# ❌ This will cause an error:
#print("Age: " + 25)

#You must convert the number first:
print("Age: " + str(25))

# Or better:

print("Age:", 25)

# Example 2: Mathematical Expressions
age = 5 * 7

#Python calculates: 5 * 7 = 35

#Now: age = 35

# Example 3: Variable on Both Sides
age = age * 2 + 3
# Let’s assume: age = 35
print(age) # we get 73

# Incrementing a Variable
age += 1
print(age) # we get 74

# Order of Operations
print(2 + 3 * 4) # 14
print((2 + 3) * 4) # 20
print(2 + (3 * 4)) # 14
