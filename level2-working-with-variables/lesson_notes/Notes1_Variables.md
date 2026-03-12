# Working with Variables in Python

Variables are one of the most fundamental concepts in programming. They allow programmers to **store, access, and manipulate data** throughout a program. In Python, variables are very flexible because the language automatically manages many technical aspects such as memory allocation and data types.

This section explains what variables are, how they work in Python, the main data types, and how to properly name variables for clean and maintainable code.

---

# 1.1 What are Variables?

In Python, **variables are names assigned to objects** that store data. A variable acts as a **label or reference** to a value stored somewhere in memory. By using variables, programmers can store information and use it later in calculations, conditions, or other operations.

Python is a **dynamically typed language**, meaning the type of a variable is determined **when a value is assigned to it**. Unlike some other languages, Python does not require explicit declaration of variable types.

Example:

```python
x = 10
```

Here:

* `x` is the variable name.
* `10` is the value assigned to the variable.

Python automatically:

* Creates the variable
* Allocates memory
* Determines that the value is an integer.

---

## 1. Declaration and Assignment

In Python, **variables do not need to be declared before use**. Assigning a value to a variable automatically creates it.

Example:

```python
x = 10
```

This single statement:

* Creates the variable `x`
* Stores the value `10`
* Determines the type (`int`)

Another example:

```python
name = "Alex"
```

Now the variable `name` stores a string value.

This automatic behavior makes Python easy to learn and write.

---

## 2. Naming Variables

Variable names must follow **Python identifier rules**.

### Rules for variable names

A variable name:

* Must start with a **letter** or **underscore**
* Cannot start with a **number**
* Cannot contain **special characters** except `_`
* Cannot be a **Python keyword**

### Good examples

```python
name1 = "Alex"
user_age = 5
total_price = 100
```

These names are valid and descriptive.

### Bad examples

```python
%city% = 7      # contains special characters
1234qwerty = 5  # starts with a number
```

These names will produce errors.

Choosing meaningful names improves code readability and makes programs easier to maintain.

---

## 3. Dynamic Typing

Python determines a variable’s type **during execution**, not before.

This means a variable can **change its type during the program**.

Example:

```python
x = 10
print(x)

x = "hello"
print(x)
```

Here:

1. `x` first stores an **integer**
2. Later it stores a **string**

Example showing multiple changes:

```python
age = "Alexander"
age = 35
age = "London"
age = 3.14
```

The variable `age` changes between:

* string
* integer
* string
* float

This flexibility is called **dynamic typing**.

---

## 4. Referential Nature of Variables

In Python, variables **do not directly store values**. Instead, they **store references to objects in memory**.

This means multiple variables can refer to the **same object**.

Example:

```python
x = [1, 2, 3]
y = x
```

Now both `x` and `y` refer to the same list.

If the list changes using one variable, the other variable sees the change.

```python
x.append(4)

print(y)
```

Output:

```
[1, 2, 3, 4]
```

Both variables refer to the same object in memory.

---

## 5. Variable Scope

The **scope of a variable** determines where it can be accessed in a program.

Python supports three main types of scope:

### Local variables

Defined inside a function and accessible only within that function.

Example:

```python
def my_function():
    x = 5
    print(x)

my_function()
```

Here `x` exists only inside the function.

---

### Global variables

Defined outside functions and accessible throughout the program.

Example:

```python
x = 10

def show_value():
    print(x)

show_value()
```

Here `x` is a global variable.

---

### Non-local variables

Used inside **nested functions** to refer to variables from an outer function.

This concept will be explored more deeply later.

---

## 6. Memory Management

Python automatically manages memory using a **garbage collector**.

This means:

* Memory is allocated when variables are created.
* Memory is freed when objects are no longer used.

Programmers do **not need to manually manage memory**, which reduces errors and simplifies development.

---

## 7. Immutability of Objects

Some Python objects are **immutable**, meaning their values **cannot be changed after creation**.

Examples of immutable types include:

* strings (`str`)
* tuples (`tuple`)

Example:

```python
text = "hello"
```

If you try to modify it, Python creates a **new object instead of changing the original one**.

Example:

```python
text = text + " world"
```

This does not modify the original string; it creates a new one.

---

## 8. Multiple Assignments

Python allows assigning **multiple variables in one line**.

Example:

```python
x, y, z = 1, 2, 3
```

This assigns:

* `x = 1`
* `y = 2`
* `z = 3`

Equivalent longer version:

```python
x = 1
y = 2
z = 3
```

Multiple assignment makes code shorter and cleaner.

---

# 1.2 Data Types

Python provides several **basic data types** for storing different kinds of data.

The most common ones are:

* `int`
* `str`
* `float`
* `bool`

These data types form the foundation for building more complex programs.

---

## int (Integers)

The `int` type represents **whole numbers without decimals**.

Integers can be:

* positive
* negative
* zero

Example:

```python
x = 5
temperature = -10
year = 2026
```

All these values are integers.

---

## str (Strings)

The `str` type stores **text data**.

Strings must be enclosed in **quotes**:

* single quotes `' '`
* double quotes `" "`

Example:

```python
name = "John"
city = 'London'
```

Strings support many operations such as:

### Concatenation (joining strings)

```python
first_name = "John"
last_name = "Smith"

full_name = first_name + " " + last_name
print(full_name)
```

Output:

```
John Smith
```

### Duplication

```python
word = "Hi "
print(word * 3)
```

Output:

```
Hi Hi Hi
```

Strings also provide many methods for manipulating text.

---

## float (Floating-Point Numbers)

The `float` type represents numbers **with decimal points**.

Example:

```python
pi = 3.14
price = 19.99
temperature = -5.5
```

Floating-point numbers are commonly used in:

* measurements
* scientific calculations
* financial data

---

## bool (Boolean Values)

The `bool` type represents **logical values**.

It has only two possible values:

* `True`
* `False`

Example:

```python
is_valid = True
is_logged_in = False
```

Booleans are commonly used in:

* conditional statements
* loops
* logical operations

Example:

```python
age = 18
is_adult = True
```

Boolean values often control program flow.

---

# 1.3 Variable Names

Variable names play a crucial role in **code readability and maintainability**. Well-chosen names help programmers understand what the code is doing.

Poor naming can make code confusing and difficult to debug.

---

## Rules for Naming Variables

### 1. Use clear and descriptive names

Variable names should reflect their purpose.

Example:

Good:

```python
count = 10
```

Better:

```python
student_count = 10
```

The second example is more descriptive.

---

### 2. Follow Python styling standards (PEP 8)

The widely accepted Python style guide recommends:

**lowercase words separated by underscores**

Example:

```python
user_name
total_price
max_height
```

This format improves readability.

---

### 3. Avoid Python keywords

Python has reserved keywords that cannot be used as variable names.

Examples include:

* `if`
* `else`
* `class`
* `return`
* `for`
* `while`

Example of incorrect code:

```python
class = 5
```

This will produce an error.

---

### 4. Use short names for small variables

In short loops or small code blocks, short variable names are acceptable.

Example:

```python
for i in range(5):
    print(i)
```

Variables like `i` or `j` are common in loops.

---

### 5. Use descriptive names for global variables

Variables used throughout a program should be **clear and descriptive**.

Example:

Good:

```python
total_price
user_age
maximum_speed
```

Bad:

```python
x
y
z
```

Clear names improve readability for everyone working on the code.

---

## Examples of Good Variable Names

```python
user_age
total_price
max_height
min_height
student_count
```

These names clearly describe the data stored in them.

---

## Special Cases

In some fields, especially **mathematics, physics, and scientific computing**, single-letter variables are standard.

Examples:

```python
x, y, z
```

These are commonly used for:

* coordinates
* mathematical formulas
* algorithms

In such contexts, short names are acceptable because they follow established conventions.

---

# Conclusion

Variables are essential components of Python programming. They allow developers to store and manipulate data efficiently while keeping programs readable and organized.

Key points to remember:

* Variables are names that reference objects in memory.
* Python uses **dynamic typing**, so variable types are determined at runtime.
* Common data types include `int`, `str`, `float`, and `bool`.
* Variables follow specific naming rules and conventions.
* Python automatically manages memory and allows flexible assignments.

Using meaningful variable names and understanding how variables work will make your programs **clearer, easier to debug, and easier to maintain**.

---

