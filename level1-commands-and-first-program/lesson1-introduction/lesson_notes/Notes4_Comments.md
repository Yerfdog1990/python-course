# Writing Comments in Python

Comments are an essential part of writing clean, professional Python code. They help explain what the code does — not to the computer, but to **people**.

The Python interpreter ignores comments completely. They are meant for:

* You (future you will be grateful)
* Other developers
* Team collaboration
* Long-term maintenance

---

# 1. How to Write Comments

## Single-Line Comments

In Python, single-line comments begin with the `#` symbol.

Everything after `#` on the same line is ignored by Python.

### Example:

```python
# This is a single-line comment
print("Hello, World!")  # Explanation of the function's action
```

What happens here?

* The first line is completely ignored.
* The comment after `print()` is also ignored.
* Only `print("Hello, World!")` is executed.

Single-line comments are typically used for:

* Short explanations
* Clarifying complex logic
* Temporary notes
* Debugging

---

## Multi-Line Comments

Python does not have official syntax specifically for multi-line comments.

However, there are two common approaches:

---

### Method 1: Multiple Single-Line Comments

```python
# This is an example of a multi-line comment
# Each line starts with the '#' symbol
# The interpreter ignores all of them
```

This is the most common and recommended approach.

---

### Method 2: Triple Quotes (Multi-Line String Literal)

```python
"""
This is a multi-line literal that can be used as a comment.
Python interprets it as a string,
but does nothing with it if it is not assigned to a variable.
"""
```

Important:

Triple-quoted text is technically a **string literal**, not a real comment.

If it is:

* Not assigned to a variable
* Not used in an expression

Then Python simply ignores it.

---

## What Is a Literal?

A **literal** is a fixed value written directly in code.

Examples:

```python
10          # Integer literal
3.14        # Float literal
"Hello"     # String literal
True        # Boolean literal
```

---

# 2. Why Write Comments?

Comments improve:

### ✔ Readability

Code becomes easier to understand.

### ✔ Maintainability

Future updates are easier.

### ✔ Team Collaboration

Other developers can understand your logic.

### ✔ Documentation

Comments explain *why* something is done — not just *what* is done.

---

## Good Comment Practices

Comments should be:

* Clear
* Brief
* Relevant
* Helpful

Avoid obvious comments like this:

```python
x = 5  # Assign 5 to x
```

That comment adds no value.

Better example:

```python
# Store the default retry limit for network requests
retry_limit = 5
```

This explains the **purpose**, not just the action.

---

# 3. Documenting Strings (Docstrings)

Docstrings are special multi-line strings used for documentation.

They are usually placed at the beginning of:

* Modules
* Classes
* Functions
* Methods

They are enclosed in triple double quotes (`""" """`).

---

## Example of a Function with a Docstring

```python
def add(a, b):
    """
    Function for adding two numbers.

    :param a: first number to add
    :param b: second number to add
    :return: sum of a and b
    """
    return a + b
```

Why use docstrings?

* They describe what the function does.
* They explain parameters.
* They explain return values.
* They can be used to automatically generate documentation.

Docstrings are professional documentation tools.

---

# 4. Funny Comments in Code

Programming is serious work — but it is also creative and human.

Sometimes developers add humorous comments:

```python
# I would explain what's going on here,
# but even I don't understand it anymore.
```

```python
# If this doesn't work, it's someone else's fault.
```

```python
# Came, saw, fixed... and broke it.
```

```python
# When I wrote this, only God and I knew how it works.
# Now only God knows.
```

```python
# Number of hours wasted here = 42.
```

These comments:

* Add personality
* Make development more enjoyable
* Remind us that coding is a human process

However, in professional environments, balance humor with clarity.

---

# 5. Quickly Comment Out Code (PyCharm Tip)

If you are using **PyCharm IDE**, you can quickly comment or uncomment selected lines.

### Windows:

```
Ctrl + /
```

### macOS:

```
Cmd + /
```

How it works:

1. Select one or more lines.
2. Press the shortcut.
3. `#` is automatically added or removed.

Example:

Before:

```python
print("Hello")
print("World")
```

After pressing the shortcut:

```python
# print("Hello")
# print("World")
```

This is extremely useful for:

* Debugging
* Testing different code blocks
* Temporarily disabling code

---

# Example: Using Comments in a Real Program

```python
# Store user information
name = "Alexander"
birth_year = 1990

# Calculate age
current_year = 2024
age = current_year - birth_year

# Display results
print("Name:", name)
print("Age:", age)
```

Notice:

The comments explain:

* What section of code does
* Why variables exist
* What the logic represents

---

# Key Takeaways

* ✔ Comments are ignored by the Python interpreter
* ✔ Single-line comments start with `#`
* ✔ Multi-line comments can be written using multiple `#` lines
* ✔ Triple quotes create string literals (often used as comments)
* ✔ Docstrings document functions, classes, and modules
* ✔ Comments improve readability and collaboration
* ✔ IDE shortcuts make commenting faster

---

# Final Thought

* Good programmers don’t just write code.
* They write code that other humans can understand.
* Comments are the bridge between logic and understanding.
* And future you will always appreciate well-commented code.
