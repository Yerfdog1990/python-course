# Getting Input from the Console in Python

In programming, interacting with the user is an important capability. One of the simplest ways programs interact with users is through the **console**.

This lesson explains:

1. What the console is
2. Console input and output
3. The `input()` function
4. Entering numbers from the console
5. Type conversion when reading input

---

# 3.1 Console

## What Is a Console?

In the early days of computing, computers were extremely large machines that users accessed through **remote terminals connected via phone networks**. These terminals were called **consoles**.

Today, the term **console** refers to a **text-based interface** where users interact with a computer by typing commands using the keyboard.

The console allows programs to:

* display information
* receive user input
* test and debug programs

---

## Console Output

Console output means **displaying information on the screen**.

In Python, the **`print()` function** is used to display output.

Example:

```python
print("This message will be displayed on the console.")
```

Output:

```
This message will be displayed on the console.
```

The `print()` function can display:

* text
* numbers
* variables
* expressions

Example:

```python
print("The result is:", 10 + 5)
```

Output:

```
The result is: 15
```

---

## Console Input

Console input means **entering data into a program using the keyboard**.

Python uses the **`input()` function** to receive data from the user.

Console interaction is very useful for:

* testing programs
* educational exercises
* automation scripts
* debugging code
* simple command-line tools

Console applications are often **easier to build and debug** than graphical applications.

---

# 3.2 The `input()` Function

The **`input()` function** is used to read data entered by the user from the keyboard.

Basic syntax:

```python
input()
```

When the program reaches this function, it **waits for the user to type something and press Enter**.

The value entered by the user is returned as **a string (`str`)**.

---

## Example: Simple Input

```python
name = input("Enter your name: ")
print("Hello", name)
```

Explanation:

1. The program asks the user to enter their name.
2. The user types their name and presses Enter.
3. The program prints a greeting using the entered name.

Example run:

```
Enter your name: Alice
Hello Alice
```

---

## Using `input()` Without a Prompt

The `input()` function can also be used **without any message**.

Example:

```python
name = input()
print("Hello", name)
```

Program execution:

```
Alice
Hello Alice
```

In this case, the program simply waits for input without displaying a prompt.

---

## Example: Multiple Inputs

Programs can ask for several pieces of information.

Example:

```python
name = input("Enter your name: ")
city = input("Enter your city: ")

print("Hello", name)
print("You live in", city)
```

Example output:

```
Enter your name: John
Enter your city: Nairobi
Hello John
You live in Nairobi
```

---

# 3.3 Entering Numbers from the Console

A very important thing to remember:

⚠ **The `input()` function always returns a string.**

This means that if the user enters a number, Python still treats it as **text**.

Example:

```python
age = input("Enter your age: ")
print(age)
```

Even if the user enters `20`, Python stores `"20"` as a **string**.

To perform mathematical operations, the string must be **converted into a numeric type**.

---

## Converting Input to an Integer

To convert input into an integer, use the **`int()` function**.

Example:

```python
age = input("Enter your age: ")
age = int(age)

print("In 10 years you will be", age + 10)
```

Example run:

```
Enter your age: 25
In 10 years you will be 35
```

---

## Shorter Version (Single Line)

Often programmers combine input and conversion into one line.

Example:

```python
age = int(input("Enter your age: "))
print("In 10 years you will be", age + 10)
```

This code performs:

1. input from the user
2. conversion to integer
3. storing the result in `age`

---

## Converting Input to a Floating Point Number

To read decimal numbers, use the **`float()` function**.

Example:

```python
price = float(input("Enter the product price: "))
print("The price with tax is", price * 1.1)
```

Example run:

```
Enter the product price: 25.5
The price with tax is 28.05
```

---

# Example Program: Simple Calculator

The following program asks the user for two numbers and adds them.

```python
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

result = num1 + num2

print("The sum is:", result)
```

Example run:

```
Enter the first number: 10
Enter the second number: 5
The sum is: 15
```

---

# Example Program: Age Calculator

```python
name = input("Enter your name: ")
age = int(input("Enter your age: "))

future_age = age + 10

print(name, "in 10 years you will be", future_age, "years old.")
```

Example run:

```
Enter your name: Alice
Enter your age: 22
Alice in 10 years you will be 32 years old.
```

---

# Input Errors

When converting input to numbers, errors can occur.

Example:

```python
age = int(input("Enter your age: "))
```

If the user enters:

```
twenty
```

Python produces an error:

```
ValueError
```

This happens because `"twenty"` cannot be converted into an integer.

Programs must handle such situations carefully.

Error handling will be discussed in later lessons.

---

# Summary

Key points to remember:

* The **console** is a text-based interface used to interact with programs.
* **Console output** displays information using `print()`.
* **Console input** reads user data using `input()`.
* The `input()` function always returns a **string**.
* To use numbers, the input must be converted using `int()` or `float()`.
* Improper input can cause errors such as **ValueError**.

Console input and output are fundamental programming skills and are widely used in:

* educational programs
* command-line tools
* automation scripts
* debugging and testing programs

---


