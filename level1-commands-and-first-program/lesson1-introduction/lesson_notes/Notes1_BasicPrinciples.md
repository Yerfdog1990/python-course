# Commands and First Program in Python

## 1. What Is a Program?

A **program** is a set (or list) of commands.

When a program runs:

1. The first command is executed.
2. Then the second.
3. Then the third.
4. And so on, until all commands are finished.

After the last command runs, the program ends.

### Who Executes the Commands?

Commands only work if the executor understands them.

For example:

* You can tell a dog 🐕: `"Sit"` or `"Speak"`
* A cat 🐈: `"Shoo!"`
* A person: `"Stop!"`
* A robot 🔧: `"Work!"`

In Python, the executor is the **Python Interpreter**.

## Python Interpreter

Programs written in Python are executed by **`py.exe`** (on Windows) or by the Python interpreter installed on your system.

The **Python Interpreter** is a special program that:

* Reads Python code
* Understands Python commands
* Executes them one by one

Without the interpreter, Python code is just text.

---

## 2. Basic Python Principles

Instead of memorizing many rules, it’s better to understand a few key principles.

### Principle 1: One Command per Line

In Python, it is customary to write each command on a new line.

Example:

```python
print("Robot is a friend of humans")
print("Robot is a friend of humans")
print("Robot is a friend of humans")
```

Each `print()` is a separate command.

The interpreter executes them from top to bottom.

---

### Principle 2: Indentation Is Extremely Important

Python uses **spaces at the beginning of a line** to define structure.

The number of spaces (indentation) matters.

This code will NOT work:

```python
print("Robot is a friend of humans")
   print("Robot is a friend of humans")
print("Robot is a friend of humans")
```

Why?

Because the second line has extra spaces. Python expects consistent indentation when grouping commands.

Unlike many other programming languages, Python does not use `{}` to define blocks. It uses **indentation** instead.

---

### Principle 3: Indentation Groups Commands into Blocks

Commands with the same indentation level belong to the same block.

Example:

```python
for name in ["Masha", "Katya", "Anya"]:
    print("Robot is a friend of humans")
    print(f"{name} is a friend of robots")
```

### What Happens Here?

1. The `for` loop goes through each name in the list.
2. The indented lines belong to the loop.
3. For each name:

   * It prints `"Robot is a friend of humans"`
   * It prints the current name using an f-string

Output:

```
Robot is a friend of humans
Masha is a friend of robots
Robot is a friend of humans
Katya is a friend of robots
Robot is a friend of humans
Anya is a friend of robots
```

The two indented `print()` statements form a **block**.

You will learn more about code blocks in future lessons.

---

## 3. Your First Python Program

Traditionally, the first program in most languages prints:

```python
print("Hello, World!")
```

But that’s too ordinary.

Your first program should be memorable.

Let’s write something more dramatic.

### Example 1

```python
print("It is inevitable. It is your destiny.")
```

### Example 2

```python
print("Do what must be done, Lord Vader.")
print("Do not hesitate.")
print("Show no mercy.")
```

### Example 3

```python
print("The dark side of the Force is a pathway")
print("to many abilities some consider to be unnatural.")
```

---

## How to Run Your First Program

1. Open your Python environment (IDLE, VS Code, PyCharm, or terminal).
2. Create a new file called:

```
first_program.py
```

3. Type your code:

```python
print("It is inevitable. It is your destiny.")
```

4. Save the file.
5. Run it using:

```bash
py first_program.py
```

or

```bash
python first_program.py
```

The interpreter reads your file and executes it line by line.

---

## Key Takeaways

* A **program** is a list of commands executed in order.
* Python programs are executed by the **Python Interpreter**.
* Each command is usually written on a new line.
* **Indentation is critical** in Python.
* Commands with the same indentation belong to the same block.
* The `print()` function displays text on the screen.
* Your first program is simply a command that prints text.

---

## Practice Exercise

### Task:

Write a program that prints a powerful three-line message of your own.

Example structure:

```python
print("Line 1")
print("Line 2")
print("Line 3")
```

### Challenge:

Modify it so that it prints your name in one of the lines using an f-string:

```python
name = "YourName"
print(f"{name} will master Python.")
```

---

You’ve just taken your first real step into programming.

From here on, every powerful application, game, AI system, or website starts the same way:

One command.
Then another.
Then another.
