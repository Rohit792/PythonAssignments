# Python Assignment 21

This assignment focuses on advanced multithreading concepts including thread synchronization, locks, shared resources, and concurrent data processing in Python.

---

## 📚 Topics Covered

- Advanced threading concepts
- Thread synchronization
- Lock mechanism
- Race condition prevention
- Shared variable management
- Concurrent list processing
- Thread communication
- Result passing between threads

---

## 🎯 Questions

### 1. Prime and Non-Prime Number Threads
Design a Python application that creates two threads named `Prime` and `NonPrime`.
- Both threads should accept a list of integers.
- The **Prime** thread should display all prime numbers from the list.
- The **NonPrime** thread should display all non-prime numbers from the list.

**Example:**
```
Input List: [12, 13, 17, 19, 22, 24, 29, 31, 37, 40]

Prime numbers: [13, 17, 19, 29, 31, 37]
Non-Prime numbers: [12, 22, 24, 40]
```

---

### 2. Maximum and Minimum Element Threads
Design a Python application that creates two threads.
- **Thread 1** should calculate and display the maximum element from a list.
- **Thread 2** should calculate and display the minimum element from the same list.
- The list should be accepted from the user.

**Example:**
```
Input List: [15, 8, 42, 3, 27, 55, 12]

Maximum element: 55
Minimum element: 3
```

---

### 3. Thread Synchronization with Lock
Design a Python application where multiple threads update a shared variable.
- Use a **Lock** to avoid race conditions.
- Each thread should increment the shared counter multiple times.
- Display the final value of the counter after all threads complete execution.

**Example:**
```
Number of threads: 5
Increments per thread: 1000

Final counter value: 5000
```

---

### 4. Sum and Product Threads
Design a Python application that creates two threads.
- **Thread 1** should compute the sum of elements from a list.
- **Thread 2** should compute the product of elements from the same list.
- Return the results to the main thread and display them.

**Example:**
```
Input List: [2, 3, 4, 5]

Sum: 14
Product: 120
```

---

## 📝 Notes

- Ensure proper thread synchronization when accessing shared resources.
- Use `threading.Lock()` to prevent race conditions.
- Use `join()` method to wait for thread completion.
- Display thread names and IDs where applicable for better tracking.