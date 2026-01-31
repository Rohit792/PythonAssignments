# Python Assignment 19

This assignment focuses on advanced lambda functions with `filter()`, `map()`, and `reduce()` for functional programming in Python.

---

## 📚 Topics Covered

- Lambda functions
- `filter()` function
- `map()` function
- `reduce()` function
- Functional programming
- List transformations
- Prime number operations

---

## 🎯 Questions

### 1. Power of Two Using Lambda
Write a program which contains one lambda function which accepts one parameter and returns the power of two (square) of that number.

**Example:**
```
Input: 4
Output: 16

Input: 6
Output: 36
```

---

### 2. Multiplication Using Lambda
Write a program which contains one lambda function which accepts two parameters and returns their multiplication.

**Example:**
```
Input: 4, 3
Output: 12

Input: 6, 3
Output: 18
```

---

### 3. Filter, Map, and Reduce - Range Operations
Write a program which contains `filter()`, `map()`, and `reduce()` functions. Python application which contains one list of numbers accepted from user.
- **Filter:** Filter out all numbers which are greater than or equal to 70 and less than or equal to 90.
- **Map:** Increase each number by 10.
- **Reduce:** Return product of all numbers.

**Example:**
```
Input List: [4, 34, 36, 76, 68, 24, 89, 23, 86, 90, 45, 70]

List after filter: [76, 89, 86, 90, 70]
List after map: [86, 99, 96, 100, 80]
Output of reduce: 6538752000
```

---

### 4. Filter, Map, and Reduce - Even Numbers
Write a program which contains `filter()`, `map()`, and `reduce()` functions. Python application which contains one list of numbers accepted from user.
- **Filter:** Filter out all even numbers.
- **Map:** Calculate square of each number.
- **Reduce:** Return addition of all numbers.

**Example:**
```
Input List: [5, 2, 3, 4, 3, 4, 1, 2, 8, 10]

List after filter: [2, 4, 4, 2, 8, 10]
List after map: [4, 16, 16, 4, 64, 100]
Output of reduce: 204
```

---

### 5. Filter, Map, and Reduce - Prime Numbers
Write a program which contains `filter()`, `map()`, and `reduce()` functions. Python application which contains one list of numbers accepted from user.
- **Filter:** Filter out all prime numbers.
- **Map:** Multiply each number by 2.
- **Reduce:** Return maximum number from those numbers.

(You can also use normal functions instead of lambda functions)

**Example:**
```
Input List: [2, 70, 11, 10, 17, 23, 31, 77]

List after filter: [2, 11, 17, 23, 31]
List after map: [4, 22, 34, 46, 62]
Output of reduce: 62
```