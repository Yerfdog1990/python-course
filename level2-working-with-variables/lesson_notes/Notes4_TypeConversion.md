# Type Conversion in Python

In Python programming, **type conversion** (also called **type casting**) is the process of converting a value from one data type to another.

For example, you may need to convert:

* a **string to a number**
* a **number to a string**
* an **integer to a decimal number**

Type conversion is very common in programs that interact with user input, perform calculations, or display formatted output.

Python provides several built-in functions for type conversion. The three main ones are:

* `int()` – converts values to integers
* `str()` – converts values to strings
* `float()` – converts values to floating-point numbers

Understanding these functions is essential for writing correct and flexible programs.

---

# 4.1 The `int()` Function

The **`int()` function** converts a value into an **integer** (a whole number).

Integers are numbers without decimal points, such as:

```
1, 10, -5, 100
```

The `int()` function can convert several data types into integers.

---

# Converting a String to an Integer

If a string contains numeric characters, it can be converted to an integer.

Example:

```python
num_str = "42"
num_int = int(num_str)
print(num_int)  # Output: 42
```

Explanation:

* `"42"` is a **string**
* `int("42")` converts it into the integer **42**

---

# Error When the String Is Not a Number

If the string does not represent a valid number, Python will raise an error.

Example:

```python
num_str = "forty two"
num_int = int(num_str)
print(num_int)  # ValueError: invalid literal for int() with base 10: 'forty two'
```

Explanation:

The text `"forty two"` cannot be interpreted as a number, so Python throws a **ValueError**.

---

# Converting a Floating-Point Number to an Integer

The `int()` function can also convert **floating-point numbers** (decimal numbers) into integers.

Example:

```python
num_float = 42.9
num_int = int(num_float)
print(num_int)  # Output: 42
```

Important rule:

⚠ When converting a float to an integer, **Python always removes the decimal part**.

Example:

```python
num_float = 1.9999
print(int(num_float))
```

Output:

```
1
```

This means the value is **not rounded**, but simply **truncated** (the decimal part is discarded).

---

# Converting Boolean Values to Integers

Boolean values can also be converted to integers.

In programming:

* `True` represents logical **1**
* `False` represents logical **0**

Example:

```python
true_bool = True
false_bool = False

print(int(true_bool))   # Output: 1
print(int(false_bool))  # Output: 0
```

Explanation:

| Boolean | Integer Result |
| ------- | -------------- |
| True    | 1              |
| False   | 0              |

---

# Summary of `int()` Conversions

| Original Value | Result |
| -------------- | ------ |
| `"42"`         | 42     |
| `42.9`         | 42     |
| `True`         | 1      |
| `False`        | 0      |

---

# 4.2 The `str()` Function

The **`str()` function** converts values into **strings**.

A string is a sequence of characters enclosed in quotes.

Examples of strings:

```
"Hello"
"42"
"Python"
```

Almost **any value in Python can be converted into a string**.

---

# Converting an Integer to a String

Example:

```python
num_int = 42
num_str = str(num_int)

print(num_str)  # Output: "42"
```

Explanation:

* `42` is a number
* `str(42)` converts it into the text `"42"`

---

# Converting a Floating-Point Number to a String

Example:

```python
num_float = 42.9
num_str = str(num_float)

print(num_str)  # Output: "42.9"
```

The decimal number becomes a **string representation**.

---

# Converting Boolean Values to Strings

Example:

```python
true_bool = True
false_bool = False

print(str(true_bool))   # Output: "True"
print(str(false_bool))  # Output: "False"
```

Explanation:

| Boolean | String Result |
| ------- | ------------- |
| True    | "True"        |
| False   | "False"       |

---

# Practical Example Using `str()`

The `str()` function is often used when combining numbers with text.

Example:

```python
age = 25
print("Your age is " + str(age))
```

Without conversion, this would cause an error because Python cannot directly combine a string and an integer.

---

# 4.3 The `float()` Function

The **`float()` function** converts a value into a **floating-point number** (a decimal number).

Floating-point numbers contain decimals, for example:

```
3.14
42.0
0.5
```

---

# Converting a String to a Floating-Point Number

Example:

```python
num_str = "42.9"
num_float = float(num_str)

print(num_float)  # Output: 42.9
```

Explanation:

The string `"42.9"` becomes the decimal number **42.9**.

---

# Converting an Integer to a Floating-Point Number

Example:

```python
num_int = 42
num_float = float(num_int)

print(num_float)  # Output: 42.0
```

Explanation:

The integer **42** becomes **42.0**.

---

# Converting Boolean Values to Floating-Point Numbers

Example:

```python
true_bool = True
false_bool = False

print(float(true_bool))   # Output: 1.0
print(float(false_bool))  # Output: 0.0
```

Explanation:

| Boolean | Float Result |
| ------- | ------------ |
| True    | 1.0          |
| False   | 0.0          |

---

# Example Program Using Type Conversion

The following program asks the user to enter numbers and performs calculations.

```python
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

sum_result = num1 + num2

print("The sum is:", sum_result)
```

Example run:

```
Enter the first number: 5
Enter the second number: 3.5
The sum is: 8.5
```

---

# Another Example: Converting Values

```python
num_str = "10"
num_int = int(num_str)
num_float = float(num_int)
num_string = str(num_float)

print(num_int)
print(num_float)
print(num_string)
```

Output:

```
10
10.0
10.0
```

---

# Summary

Type conversion allows Python programs to **transform values between different data types**.

The three most important conversion functions are:

| Function  | Purpose                                     |
| --------- | ------------------------------------------- |
| `int()`   | Converts a value to an integer              |
| `str()`   | Converts a value to a string                |
| `float()` | Converts a value to a floating-point number |

Important points:

* `int()` removes the decimal part when converting floats.
* `str()` converts almost any value into text.
* `float()` converts values into decimal numbers.
* Invalid conversions may cause errors such as **ValueError**.

Type conversion is widely used when:

* reading user input
* performing mathematical calculations
* formatting output
* combining text with numbers

Mastering these functions helps programmers write **more flexible and reliable programs**.

---


