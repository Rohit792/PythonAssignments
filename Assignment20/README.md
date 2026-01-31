# Python Assignment 20

This assignment focuses on multithreading in Python, covering thread creation, execution, synchronization, and working with shared resources.

---

## 📚 Topics Covered

- Threading module
- Thread creation and execution
- Thread synchronization
- Concurrent execution
- Thread communication
- Shared variables and locks
- Thread attributes (ID, Name)

---

## 🎯 Questions

### 1. Even and Odd Threads
Design a Python application that creates two separate threads named `Even` and `Odd`.
- The **Even** thread should display the first 10 even numbers.
- The **Odd** thread should display the first 10 odd numbers.
- Both threads should execute independently using the threading module.
- Ensure proper thread creation and execution.

**Example:**
```
Even numbers: 0, 2, 4, 6, 8, 10, 12, 14, 16, 18
Odd numbers: 1, 3, 5, 7, 9, 11, 13, 15, 17, 19
```

---

### 2. Even and Odd Factor Threads
Design a Python application that creates two threads named `EvenFactor` and `OddFactor`.
- Both threads should accept one integer number as a parameter.
- The **EvenFactor** thread should:
  - Identify all even factors of the given number.
  - Calculate and display the sum of even factors.
- The **OddFactor** thread should:
  - Identify all odd factors of the given number.
  - Calculate and display the sum of odd factors.
- After both threads complete execution, the main thread should display the message: "Exit from main"

**Example:**
```
Input: 12
Even factors: 2, 4, 6, 12 → Sum = 24
Odd factors: 1, 3 → Sum = 4
Exit from main
```

---

### 3. Even and Odd List Threads
Design a Python application that creates two threads named `EvenList` and `OddList`.
- Both threads should accept a list of integers as input.
- The **EvenList** thread should:
  - Extract all even elements from the list.
  - Calculate and display their sum.
- The **OddList** thread should:
  - Extract all odd elements from the list.
  - Calculate and display their sum.
- Threads should run concurrently.

**Example:**
```
Input List: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Even elements sum: 30
Odd elements sum: 25
```

---

### 4. Character Classification Threads
Design a Python application that creates three threads named `Small`, `Capital`, and `Digits`.
- All threads should accept a string as input.
- The **Small** thread should count and display the number of lowercase characters.
- The **Capital** thread should count and display the number of uppercase characters.
- The **Digits** thread should count and display the number of numeric digits.
- Each thread must also display:
  - Thread ID
  - Thread Name

**Example:**
```
Input: "Hello123World"
Small: 8 lowercase characters
Capital: 2 uppercase characters
Digits: 3 numeric digits
```

---

### 5. Sequential Thread Execution
Design a Python application that creates two threads named `Thread1` and `Thread2`.
- **Thread1** should display numbers from 1 to 50.
- **Thread2** should display numbers from 50 to 1 in reverse order.
- Ensure that:
  - Thread2 starts execution only after Thread1 has completed.
- Use appropriate thread synchronization.

**Example:**
```
Thread1: 1, 2, 3, ..., 50
Thread2: 50, 49, 48, ..., 1
```

