# Python Exception Handling with Functions

## 📌 Overview

This project demonstrates how to implement **exception handling within functions** in Python. The program accepts two integer inputs from the user and performs integer division using a separate function. It handles invalid inputs and division-by-zero errors gracefully without terminating the program unexpectedly.

This example is useful for understanding how exception handling can be distributed across different parts of a program.

---

## 🚀 Features

* Accepts two integer values from the user
* Performs integer division using a custom function
* Handles division-by-zero exceptions inside the function
* Handles invalid user input in the main program
* Demonstrates modular programming with functions
* Beginner-friendly implementation

---

## 🛠️ Technologies Used

* Python 3

---

## 📂 Project Structure

```text
├── division_function.py
├── README.md
```

---

## 💻 Source Code

```python
def division(x, y):
    try:
        d = x // y
        print("Division is", d)

    except ZeroDivisionError:
        print("Error in data : Divisor should not be zero")


print("Program starts...")

try:
    a = int(input("Enter first number : "))
    b = int(input("Enter second number : "))

    division(a, b)

except ValueError:
    print("Error in data : Number not provided correctly")

print("Program ends...")
```

---

## ▶️ How to Run

### Clone the Repository

```bash
git clone https://github.com/your-username/python-exception-handling-functions.git
cd python-exception-handling-functions
```

### Run the Program

```bash
python division_function.py
```

---

## 📋 Sample Outputs

### Successful Execution

```text
Program starts...
Enter first number : 20
Enter second number : 5
Division is 4
Program ends...
```

### Division by Zero

```text
Program starts...
Enter first number : 20
Enter second number : 0
Error in data : Divisor should not be zero
Program ends...
```

### Invalid Input

```text
Program starts...
Enter first number : abc
Error in data : Number not provided correctly
Program ends...
```

---

## 🧠 Concepts Covered

* Functions in Python
* Exception Handling
* `try-except` Blocks
* `ZeroDivisionError`
* `ValueError`
* Integer Division (`//`)
* Modular Programming

---

## 🔍 Exception Flow

### Main Program

Handles:

```python
ValueError
```

Occurs when the user enters non-numeric data.

### Division Function

Handles:

```python
ZeroDivisionError
```

Occurs when attempting to divide by zero.

This separation of responsibilities makes the code cleaner and easier to maintain.

---

## 🎯 Learning Objectives

After completing this project, you will understand:

* How to create and call functions
* How exceptions propagate through function calls
* How to handle exceptions at different levels of a program
* Best practices for writing robust Python applications

---

## 🔮 Future Improvements

* Support floating-point division
* Return values instead of printing directly
* Add logging for exceptions
* Implement a menu-driven calculator
* Use custom exception classes

---

## 👨‍💻 Author

**Pranay Jadhao**

Electronics & Telecommunication Engineer

Aspiring Software & Embedded Systems Engineer

---

## 📄 License

This project is open-source and available for educational and learning purposes.

<img width="525" height="283" alt="image" src="https://github.com/user-attachments/assets/07e753c5-ebc6-4ef7-8c47-3e2def632b43" />
