# Variables in Python

Variables are one of the most important concepts in programming. Almost everything you do in Python involves variables.

---

# 1. Variables and Boxes

A **variable** is used to store data.

You can think of a variable like a **box**.

Imagine this:

* You write the number `13` on a piece of paper.
* You put that paper inside a box.
* Now you can say:
  👉 *The box stores the value 13.*

That’s exactly how variables work.

---

## Two Important Properties of a Variable

Every variable in Python has:

1. **A name**
2. **A value**

### 1️⃣ The Name

The name is like a **label on the box**.

It allows you to tell one variable apart from another.

Example:

```python
age
name
city
```

---

### 2️⃣ The Value

The value is the actual data stored inside the variable.

Example:

```python
age = 35
```

Here:

* `age` → variable name
* `35` → value stored inside

---

## What About Types?

Every object in Python has a **type**.

Some common types:

* Integer → `5`, `13`, `100`
* Float → `3.14`, `2.5`
* Text (string) → `"Hello"`
* Boolean → `True`, `False`

Important idea:

👉 A **variable itself does NOT have a fixed type.**

It simply stores whatever value you put into it.

Just like a real box:

* Today it can hold books.
* Tomorrow it can hold shoes.

In Python:

```python
x = 10        # x stores an integer
x = "Hello"   # now x stores a string
```

The variable `x` changed what it stores.

---

# 2. Creating Variables

In Python, you do NOT need to declare variables before using them.

You simply write:

```python
name = value
```

The `=` symbol is called the **assignment operator**.

⚠️ It does NOT mean “equals” like in math.

It means:

👉 Take the value on the right
👉 Put it into the variable on the left

---

## Examples

```python
name = "Alexander"
age = 35
city = "London"
pi = 3.14
```

What happens here?

* `name` stores a string
* `age` stores an integer
* `city` stores a string
* `pi` stores a floating-point number

Again:

A variable does not have a predefined type.
It simply stores whatever object you assign to it.

---

# 3. Expressions and Operators

On the **left side** of `=` → there must be a variable name.

On the **right side** → you can put:

* A value
* Or an expression

An **expression** is something Python can calculate.

---

## Example 1: String Concatenation

```python
name = "Alex" + "Alex"
```

Result:

```
"AlexAlex"
```

Using `+` with strings joins them together.
This is called **concatenation**.

Important rule:

You can only concatenate **string + string**.

❌ This will cause an error:

```python
print("Age: " + 25)
```

Because you cannot add string and number directly.

You must convert the number first:

```python
print("Age: " + str(25))
```

Or better:

```python
print("Age:", 25)
```

---

## Example 2: Mathematical Expressions

```python
age = 5 * 7
```

Python calculates:

```
5 * 7 = 35
```

Now:

```
age = 35
```

---

## Example 3: Variable on Both Sides

```python
age = age * 2 + 3
```

Let’s assume:

```
age = 35
```

Step-by-step:

1. Calculate `age * 2` → `70`
2. Add `3` → `73`
3. Store result in `age`

Now:

```
age = 73
```

---

## Incrementing a Variable

```python
age = age + 1
```

This means:

1. Take current value of `age`
2. Add `1`
3. Store the result back in `age`

If:

```
age = 73
```

After the command:

```
age = 74
```

Important:

This is NOT math equality.

It does NOT mean:

```
age equals age + 1
```

Instead it means:

👉 Calculate right side
👉 Assign result to left side

---

# Order of Operations

Python follows normal math rules:

1. Parentheses first
2. Multiplication and division
3. Addition and subtraction

Example:

```python
result = 2 + 3 * 4
```

Multiplication first:

```
3 * 4 = 12
2 + 12 = 14
```

So:

```
result = 14
```

If you want a different order:

```python
result = (2 + 3) * 4
```

Now:

```
2 + 3 = 5
5 * 4 = 20
```

---

# Full Example Program

```python
name = "Alexander"
birth_year = 1990
current_year = 2024

age = current_year - birth_year

print("Name:", name)
print("Birth year:", birth_year)
print("Age:", age)
```

What happens:

1. Variables are created
2. Expression is calculated
3. Results are printed

---

# Key Takeaways

* ✔ A variable is like a box
* ✔ Every variable has a name and a value
* ✔ The `=` symbol means assignment, not equality
* ✔ The right side of `=` can be an expression
* ✔ Variables can appear on both sides of assignment
* ✔ Python follows normal mathematical order of operations
* ✔ Variables do not have fixed types

---

# Practice Exercises

### Exercise 1

Create variables:

* Your name
* Your birth year
* Current year

Calculate your age and print everything.

---

### Exercise 2

What will this print?

```python
x = 10
x = x * 2
x = x + 5
print(x)
```

Step-by-step:

```
10 * 2 = 20
20 + 5 = 25
```

Output:

```
25
```

---

# Final Thought

Variables are the foundation of programming.

Without variables:

* No calculations
* No memory
* No data storage
* No real programs

They are the boxes that hold the entire world of your program.

And now — you know how to use them.

---