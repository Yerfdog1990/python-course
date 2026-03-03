# Writing Code in Python

Now that you understand what a program is and how commands are executed, it’s time to start **writing code** yourself.

We’ll begin with one of the most important and frequently used functions in Python:

```python
print()
```

---

# 1. Printing Text

The `print()` function is used to display information on the screen.

### Printing Text (Strings)

Text must be written inside quotes:

```python
print("Alexander")
```

Quotes (`" "`) tell Python that what’s inside is **text** (also called a *string*).

If you forget the quotes:

```python
print(Alexander)
```

Python will produce an error because it thinks `Alexander` is a variable name.

---

### Printing Numbers

Numbers do **not** need quotes.

Example:

```python
print(1985)
```

This prints the number `1985`.

Important:

* `"1985"` → text
* `1985` → number

Quotes are part of the text, but they are **not printed**.

---

### Example: Print Your Name and Year of Birth

```python
print("Alexander")
print(1985)
```

Output:

```
Alexander
1985
```

Each `print()` call outputs on a new line.

---

# 2. Advanced Printing

Python allows you to print **multiple objects in one line**.

To do this, separate them with commas.

### Example 1: Printing Multiple Values

```python
print("Galaxy", "NGC", 1300, "was discovered in", 1835)
```

Output:

```
Galaxy NGC 1300 was discovered in 1835
```

Python automatically:

* Converts numbers to text when needed
* Adds spaces between comma-separated values

---

## Printing Expressions

You can also print the result of calculations directly.

Example:

```python
print("Today I'm", 2024 - 1990, "years old")
```

Here’s what happens:

1. Python calculates `2024 - 1990`
2. The result is `34`
3. That result is printed

Output:

```
Today I'm 34 years old
```

Notice:

* `2024 - 1990` is an **expression**
* Python evaluates it before printing

---

## Example: Print Your Real Age

```python
print("I was born in", 2005)
print("Today I'm", 2024 - 2005, "years old")
```

Python calculates automatically. No need to use a calculator.

---

# Understanding What Happens Internally

When Python sees:

```python
print("Hello", 5 + 3)
```

It:

1. Calculates `5 + 3`
2. Converts the result to text
3. Prints everything with spaces

Output:

```
Hello 8
```

---

# 3. Cats and Boxes (Introduction to Variables)

Here’s a funny idea:

How to catch a cat:

1. Get an empty box.
2. Wait.

😄

But here’s the important programming idea:

You can put many cats in a box.
But in programming, a **variable** can store only one value at a time.

A variable is like a labeled box.

Example:

```python
name = "Alexander"
year = 1985
```

Here:

* `name` stores `"Alexander"`
* `year` stores `1985`

You can then print them:

```python
print(name)
print(year)
```

Or combine them:

```python
print(name, "was born in", year)
```

Output:

```
Alexander was born in 1985
```

---

# Key Concepts Learned

### 1. Text must be inside quotes

```python
print("Hello")
```

### 2. Numbers do not need quotes

```python
print(2024)
```

### 3. Multiple items can be printed using commas

```python
print("Age:", 34)
```

### 4. Python evaluates expressions before printing

```python
print(10 + 5)
```

### 5. Variables store one value at a time

```python
age = 20
```

---

# Practice Exercises

### Exercise 1

Write a program that prints:

* Your name
* Your birth year
* Your age (calculated automatically)

Example solution:

```python
name = "John"
birth_year = 2006

print(name)
print("Born in", birth_year)
print("Age:", 2024 - birth_year)
```

---

### Exercise 2

Print this sentence in one line using commas:

```
My name is Alex and I love Python
```

Solution:

```python
print("My name is", "Alex", "and I love Python")
```

---

# Final Thought

Writing code starts simple:

* Print text
* Print numbers
* Print expressions
* Store values in variables

Every complex program in the world starts with simple commands like these.

And now — you’re writing real Python code.
