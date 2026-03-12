# 5. Comments in Code (Python)

Comments are an essential part of writing clean, understandable, and maintainable programs. While computers execute code, **humans read and maintain it**, so comments help explain what the code does and why it exists.

In Python, comments allow programmers to include explanations and notes directly inside the source code without affecting program execution.

---

# 5.1 How to Write Comments

In Python, comments are written using the **`#` symbol** or **triple quotes (`""" """`)** depending on the situation.

Comments are ignored by the Python interpreter, meaning they **do not affect how the program runs**.

They are mainly used to:

* Explain complex logic
* Describe the purpose of code
* Provide reminders for developers
* Improve collaboration within a team

---

## 1. Single-line Comments

A **single-line comment** begins with the **`#` symbol**.

Everything written after `#` on the same line is treated as a comment and ignored by Python.

This type of comment is typically used for:

* Short explanations
* Clarifying a specific line of code
* Adding notes

### Example

```python
# This is a single-line comment
print("Hello, World!")  # Explanation of what this line does
```

Explanation:

* `# This is a single-line comment` explains something about the code.
* `# Explanation of what this line does` describes the purpose of the `print()` function.

Python executes only:

```python
print("Hello, World!")
```

---

## 2. Multi-line Comments

Python **does not have a dedicated multi-line comment syntax** like some other languages (for example, `/* */` in Java or C).

However, you can create multi-line comments in two ways.

---

### Method 1: Multiple Single-line Comments

The most common and recommended approach is using several `#` symbols.

```python
# This is an example of a multi-line comment
# Each line starts with the # symbol
# It is used to describe multiple lines of logic
```

This approach is preferred because it clearly indicates that the lines are comments.

---

### Method 2: Triple Quotes

Another way is using **triple quotes** (`""" """` or `''' '''`).

```python
"""
This is a multi-line string literal
that can be used as a comment.
Python reads it as a string,
but it does nothing with it
if it is not assigned to a variable.
"""
```

Important note:

Triple quotes technically create a **multi-line string**, not a true comment. Python simply ignores it if it is not used.

Therefore, it is **better practice to use `#` for comments** unless writing **docstrings**.

---

# 5.2 Why Write Comments

Writing comments is a good programming habit and improves code quality.

Comments make programs easier to:

### 1. Read

Well-commented code helps developers understand what the program is doing.

Example:

```python
# Calculate the total price including tax
total_price = price + tax
```

Without the comment, the purpose might not be obvious.

---

### 2. Maintain

Programs are often modified months or years later. Comments help developers remember how the code works.

Example:

```python
# Fix for login issue when username contains spaces
username = username.strip()
```

---

### 3. Collaborate

In team projects, comments help other programmers understand your work.

They explain:

* the purpose of code
* the logic behind decisions
* special cases or warnings

---

### Best Practices for Writing Comments

Good comments should be:

* ✔ **Clear** – easy to understand
* ✔ **Short** – not overly long
* ✔ **Relevant** – explain important logic

Bad comments:

```python
# Add 1 to x
x = x + 1
```

This comment is unnecessary because the code is already obvious.

Better comments explain **why**, not just **what**.

---

# Docstrings

A **docstring** is a special type of comment used to document:

* Modules
* Classes
* Functions
* Methods

Docstrings are written using **triple double quotes (`""" """`)** and placed **at the beginning of the code block**.

They describe what the code does and how to use it.

---

### Example of a Function with a Docstring

```python
def add(a, b):
    """
    Function to add two numbers.

    :param a: first addend
    :param b: second addend
    :return: sum of a and b
    """
    return a + b
```

Explanation:

* The docstring explains the function’s purpose.
* `:param` describes parameters.
* `:return:` explains what the function returns.

Docstrings are useful because documentation tools can automatically generate documentation from them.

Example tools include:

* Sphinx
* PyDoc

---

# Funny Comments in Code

Sometimes developers add humorous comments to lighten the development process. While comments are mainly for documentation, a little humor can make the code more enjoyable to read.

Here are some examples:

### Example 1

```python
# I would explain what's going on here, but I don't understand anymore.
```

### Example 2

```python
# If this doesn't work, it's someone else's fault.
```

### Example 3

```python
# Came, saw, fixed... and broke.
```

### Example 4

```python
# When I wrote this, only God and I knew how it works.
# Now only God knows.
```

These comments reflect a common reality in programming: sometimes code becomes complicated, and even the original author may struggle to understand it later.

However, in professional environments, comments should remain **helpful and meaningful**, with humor used sparingly.

---

# 5.3 Quickly Comment Code

Most modern code editors allow developers to **quickly comment or uncomment code using keyboard shortcuts**.

In **PyCharm**, you can comment multiple lines at once.

### Steps

1. Select the lines of code you want to comment.
2. Use the keyboard shortcut.

| Operating System | Shortcut   |
| ---------------- | ---------- |
| Windows          | `Ctrl + /` |
| macOS            | `Cmd + /`  |

This shortcut automatically:

* Adds `#` to each selected line
* Removes `#` if the line is already commented

---

### Example

Original code:

```python
print("Hello")
print("World")
```

Select both lines and press **Ctrl + /**.

Result:

```python
# print("Hello")
# print("World")
```

Press the shortcut again to **uncomment** them.

---

# Summary

Comments are an important tool for writing clear and maintainable Python code.

Key points:

* Comments explain code and help developers understand programs.
* Single-line comments start with `#`.
* Python does not have true multi-line comments, but you can use multiple `#`.
* Triple quotes create multi-line strings and are mainly used for **docstrings**.
* Docstrings document functions, classes, and modules.
* IDEs like **PyCharm** provide shortcuts (`Ctrl + /`) to quickly comment code.

Well-written comments make programs easier to **read, maintain, debug, and collaborate on**, which is why they are a fundamental part of professional programming.

---


