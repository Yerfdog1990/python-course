# Python Operators

Operators are **special symbols used to perform operations on variables and values**. In Python, operators allow programmers to perform tasks such as mathematical calculations, comparisons, and updating variable values.

Operators are essential for writing programs that **process data, make decisions, and control program flow**.

The main operator categories covered here include:

1. Mathematical Operators
2. Shortcut Assignment Operators
3. Comparison Operators

---

# 2.1 Mathematical Operators

Mathematical operators are used to perform **arithmetic calculations** on numbers. Python supports the four standard arithmetic operators along with additional useful ones.

## 1. Addition (+)

The **addition operator** adds two numbers together.

```python
a = 5
b = 3
result = a + b
print(result)
```

Output

```
8
```

---

## 2. Subtraction (-)

The **subtraction operator** subtracts one number from another.

```python
a = 10
b = 4
result = a - b
print(result)
```

Output

```
6
```

---

## 3. Multiplication (*)

The **multiplication operator** multiplies two numbers.

```python
a = 6
b = 3
result = a * b
print(result)
```

Output

```
18
```

---

## 4. Regular Division (/)

The **division operator `/`** divides the first number by the second.
The result is **always a floating-point number (decimal)**.

Example

```python
result = 5 / 2
print(result)
```

Output

```
2.5
```

Even if both numbers are integers, the result will still be a **float**.

Example

```python
print(10 / 5)
```

Output

```
2.0
```

---

## 5. Integer Division (//)

The **integer division operator `//`** divides numbers and returns only the **whole number part** (without decimals).

Example

```python
result = 7 // 2
print(result)
```

Output

```
3
```

Explanation

```
7 ÷ 2 = 3.5
```

Integer division removes the decimal part and returns **3**.

Example

```python
print(10 // 3)
```

Output

```
3
```

---

## 6. Remainder (%)

The **modulus operator `%`** returns the **remainder of a division**.

Example

```python
result = 5 % 3
print(result)
```

Output

```
2
```

Explanation

```
5 ÷ 3 = 1 remainder 2
```

More examples

```python
print(10 % 3)
print(8 % 2)
```

Output

```
1
0
```

The remainder is **0 when a number is evenly divisible**.

---

## 7. Exponentiation (**)

The **exponentiation operator `**`** raises a number to a power.

Example

```python
result = 5 ** 3
print(result)
```

Output

```
125
```

Explanation

```
5³ = 5 × 5 × 5 = 125
```

Another example

```python
print(2 ** 4)
```

Output

```
16
```

---

# Summary of Mathematical Operators

| Operator | Name             | Example | Result |
| -------- | ---------------- | ------- | ------ |
| +        | Addition         | 5 + 3   | 8      |
| -        | Subtraction      | 5 - 3   | 2      |
| *        | Multiplication   | 5 * 3   | 15     |
| /        | Division         | 5 / 2   | 2.5    |
| //       | Integer Division | 7 // 2  | 3      |
| %        | Remainder        | 5 % 3   | 2      |
| **       | Exponentiation   | 5 ** 3  | 125    |

---

# 2.2 Shortcut Assignment Operators

Shortcut assignment operators allow you to **update the value of a variable quickly**.

Instead of writing long expressions, Python provides **shorter and cleaner syntax**.

Example

Normal assignment:

```python
x = 5
x = x + 1
```

Shortcut assignment:

```python
x = 5
x += 1
```

Both produce the same result.

---

## Addition Assignment (+=)

Adds a value to the variable.

```python
x = 5
x += 3
print(x)
```

Output

```
8
```

Equivalent to

```python
x = x + 3
```

---

## Subtraction Assignment (-=)

Subtracts a value from the variable.

```python
x = 5
x -= 3
print(x)
```

Output

```
2
```

Equivalent to

```python
x = x - 3
```

---

## Multiplication Assignment (*=)

Multiplies the variable by a value.

```python
x = 5
x *= 3
print(x)
```

Output

```
15
```

Equivalent to

```python
x = x * 3
```

---

## Division Assignment (/=)

Divides the variable by a value.
The result is **always a float**.

Example

```python
x = 5
x /= 2
print(x)
```

Output

```
2.5
```

---

## Integer Division Assignment (//=)

Performs integer division and stores the result.

Example

```python
x = 5
x //= 2
print(x)
```

Output

```
2
```

---

## Remainder Assignment (%=)

Stores the remainder of a division.

Example

```python
x = 5
x %= 3
print(x)
```

Output

```
2
```

---

## Exponentiation Assignment (**=)

Raises a variable to a power and stores the result.

Example

```python
x = 5
x **= 3
print(x)
```

Output

```
125
```

---

# Summary of Shortcut Assignment Operators

| Operator | Example | Equivalent |
| -------- | ------- | ---------- |
| +=       | x += 3  | x = x + 3  |
| -=       | x -= 3  | x = x - 3  |
| *=       | x *= 3  | x = x * 3  |
| /=       | x /= 3  | x = x / 3  |
| //=      | x //= 3 | x = x // 3 |
| %=       | x %= 3  | x = x % 3  |
| **=      | x **= 3 | x = x ** 3 |

---

# 2.3 Comparison Operators

Comparison operators are used to **compare two values**.

They return a **Boolean value**:

* `True`
* `False`

These operators are widely used in:

* conditional statements
* loops
* program logic

---

## Equality (==)

Checks if two values are equal.

Example

```python
print(5 == 5)
```

Output

```
True
```

Example

```python
print(5 == 3)
```

Output

```
False
```

---

## Not Equal (!=)

Checks if two values are different.

Example

```python
print(5 != 5)
```

Output

```
False
```

Example

```python
print(5 != 3)
```

Output

```
True
```

---

## Greater Than (>)

Checks if the first value is greater than the second.

Example

```python
print(5 > 3)
```

Output

```
True
```

---

## Less Than (<)

Checks if the first value is less than the second.

Example

```python
print(5 < 3)
```

Output

```
False
```

---

## Greater Than or Equal To (>=)

Checks if the first value is greater than **or equal to** the second.

Example

```python
print(5 >= 5)
```

Output

```
True
```

---

## Less Than or Equal To (<=)

Checks if the first value is less than **or equal to** the second.

Example

```python
print(5 <= 4)
```

Output

```
False
```

---

# Summary of Comparison Operators

| Operator | Meaning          | Example | Result |
| -------- | ---------------- | ------- | ------ |
| ==       | Equal            | 5 == 5  | True   |
| !=       | Not equal        | 5 != 5  | False  |
| >        | Greater than     | 5 > 3   | True   |
| <        | Less than        | 5 < 3   | False  |
| >=       | Greater or equal | 5 >= 5  | True   |
| <=       | Less or equal    | 5 <= 4  | False  |

---

# Example Program Using Operators

```python
a = 10
b = 3

print("Addition:", a + b)
print("Division:", a / b)
print("Integer Division:", a // b)
print("Remainder:", a % b)
print("Exponent:", a ** b)

print("Is a greater than b?", a > b)
print("Is a equal to b?", a == b)
```

Output

```
Addition: 13
Division: 3.3333333333333335
Integer Division: 3
Remainder: 1
Exponent: 1000
Is a greater than b? True
Is a equal to b? False
```

---

# Key Points

* Operators perform actions on variables and values.
* Mathematical operators perform arithmetic calculations.
* Shortcut assignment operators update variable values quickly.
* Comparison operators compare values and return Boolean results.
* These operators are essential for creating **conditions, calculations, and logic in programs**.

---


