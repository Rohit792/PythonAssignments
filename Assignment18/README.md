# Python Assignment 18

This assignment focuses on list operations, custom modules, and working with collections in Python.

---

## 📚 Topics Covered

- List operations
- Maximum and minimum finding
- Frequency counting
- User-defined modules
- Prime number operations
- List manipulation

---

## 🎯 Questions

### 1. Sum of List Elements
Write a program which accepts N numbers from user and stores them into a List. Return the addition of all elements from that List.

**Example:**
```
Input: 
Number of elements: 6
Elements: 13 5 45 7 4 56

Output: 130
```

---

### 2. Maximum Element from List
Write a program which accepts N numbers from user and stores them into a List. Return the maximum number from that List.

**Example:**
```
Input: 
Number of elements: 7
Elements: 13 5 45 7 4 56 34

Output: 56
```

---

### 3. Minimum Element from List
Write a program which accepts N numbers from user and stores them into a List. Return the minimum number from that List.

**Example:**
```
Input: 
Number of elements: 4
Elements: 13 5 45 7

Output: 5
```

---

### 4. Frequency of Element in List
Write a program which accepts N numbers from user and stores them into a List. Accept one another number from user and return the frequency of that number from the List.

**Example:**
```
Input: 
Number of elements: 11
Elements: 13 5 45 7 4 56 5 34 2 5 65
Element to search: 5

Output: 3
```

---

### 5. Sum of Prime Numbers from List
Write a program which accepts N numbers from user and stores them into a List. Return the addition of all prime numbers from that List. 

Main Python file accepts N numbers from user and passes each number to `ChkPrime()` function which is part of a user-defined module named as `MarvellousNum`. Name of the function from main Python file should be `ListPrime()`.

**Example:**
```
Input: 
Number of elements: 11
Elements: 13 5 45 7 4 56 10 34 2 5 8

Output: 32
```
**Explanation:** Prime numbers: 13, 5, 7, 2, 5 → 13 + 5 + 7 + 2 + 5 = 32