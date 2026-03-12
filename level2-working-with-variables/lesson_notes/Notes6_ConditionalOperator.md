# 6. Conditional Operator in Python

In programming, instructions do not always execute strictly from top to bottom. Often, a program needs to **make decisions** and perform different actions depending on certain conditions. This is where **conditional operators** come in.

A **conditional operator** allows a program to execute specific blocks of code **based on whether a condition is true or false**.

Python provides several forms of conditional statements:

* `if ... else`
* `if` (without `else`)
* `if ... elif ... else`

These structures allow programs to make decisions dynamically based on user input, calculations, or program state.

---

# 6.1 `if else`

The **`if else` statement** is the most basic form of conditional execution.

It allows a program to perform **one action if a condition is true**, and **another action if the condition is false**.

### General Syntax

```python
if condition:
    command1
else:
    command2
```

### How it works

1. Python evaluates the **condition**.
2. If the condition is **True**, the code under `if` executes.
3. If the condition is **False**, the code under `else` executes.

Important rule:

**Only one branch will execute — never both.**

---

## Indentation Rule (Very Important)

In Python, blocks of code must be **indented**.

Commands inside `if` or `else` must be indented **by 4 spaces** relative to the `if` or `else` statement.

Example:

```python
y = 4

if y > 5:
    print("y is greater than 5")
else:
    print("y is not greater than 5")
```

### Explanation

* `y = 4`
* The condition `y > 5` is evaluated.
* Since `4 > 5` is **False**, the program executes the `else` branch.

### Output

```
y is not greater than 5
```

---

## Example with User Input

Conditional operators are commonly used with **user input**.

```python
age = int(input("Enter your age:"))

if age >= 18:
    print("you are an adult")
else:
    print("go do your homework")
```

### Explanation

1. The program asks the user to enter their age.
2. The input is converted to an integer using `int()`.
3. Python checks the condition `age >= 18`.

If the age is **18 or older**, the program prints:

```
you are an adult
```

Otherwise, it prints:

```
go do your homework
```

---

# 6.2 `if` Without `else`

The **shorthand form** of a conditional statement uses only `if` and does not include an `else` branch.

### Syntax

```python
if condition:
    command
```

### How it works

* If the condition is **True**, the command executes.
* If the condition is **False**, **nothing happens** and the program continues with the next instruction.

---

## Example

```python
age = int(input("Enter your age:"))

if age >= 21:
    print("Here's your beer!")
```

### Explanation

* The program checks if the user is **21 years or older**.
* If the condition is true, the message is printed.

Example output when the user enters `25`:

```
Here's your beer!
```

If the user enters `18`, nothing is printed.

The program simply continues to the next line of code (if there is one).

---

# 6.3 `if elif else`

Sometimes programs must evaluate **multiple conditions**, not just two possibilities.

This is where the **extended conditional structure** comes in:

```python
if condition1:
    command1
elif condition2:
    command2
elif conditionN:
    commandN
else:
    commandElse
```

The keyword **`elif`** stands for **"else if"**.

This structure allows a program to check multiple conditions **in sequence**.

### How it works

Python checks the conditions **from top to bottom**.

1. If `condition1` is **True**, `command1` runs and the rest are skipped.
2. If `condition1` is **False**, Python checks `condition2`.
3. This continues until a condition is **True**.
4. If none are true, the **`else` block executes**.

Only **one block** executes.

---

## Example: Determining a Quadrant

Suppose we want to determine the **quadrant of a point on a coordinate plane**.

First, let's look at a **nested `if` version**.

```python
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
```

### Explanation

The program checks coordinates `(x, y)`:

| Condition       | Quadrant        |
| --------------- | --------------- |
| x > 0 and y > 0 | First Quadrant  |
| x < 0 and y > 0 | Second Quadrant |
| x < 0 and y < 0 | Third Quadrant  |
| x > 0 and y < 0 | Fourth Quadrant |

However, nested `if` statements quickly become **hard to read**.

---

## Improved Version Using `elif`

Python introduced `elif` to make such chains **cleaner and easier to read**.

```python
x, y = 5, -8

if x > 0 and y > 0:
    print("first quadrant")
elif x < 0 and y > 0:
    print("second quadrant")
elif x < 0 and y < 0:
    print("third quadrant")
else:
    print("fourth quadrant")
```

### Explanation

Python checks the conditions in order:

1. `x > 0 and y > 0`
2. `x < 0 and y > 0`
3. `x < 0 and y < 0`
4. Otherwise → `fourth quadrant`

Since `x = 5` and `y = -8`:

* `x > 0` → True
* `y < 0` → True

So the output is:

```
fourth quadrant
```

---

# Key Rules for Conditional Operators

### 1. Conditions must evaluate to `True` or `False`

Example:

```python
if number > 10:
```

---

### 2. Indentation defines the block

Python uses indentation instead of braces `{}` like Java.

Correct:

```python
if x > 5:
    print("greater")
```

Incorrect:

```python
if x > 5:
print("greater")
```

---

### 3. Only one branch executes

In `if-elif-else`, once Python finds a **True condition**, the remaining conditions are skipped.

---

# Summary

Conditional operators allow Python programs to **make decisions and execute code selectively**.

The main conditional structures are:

### `if else`

Used when there are **two possible outcomes**.

```python
if condition:
    command1
else:
    command2
```

---

### `if`

Used when an action should occur **only if a condition is true**.

```python
if condition:
    command
```

---

### `if elif else`

Used when there are **multiple conditions to check**.

```python
if condition1:
    command1
elif condition2:
    command2
else:
    command3
```

These structures are fundamental to programming and are used in nearly every real-world application, from **input validation** to **game logic** and **decision-making systems**.

---


