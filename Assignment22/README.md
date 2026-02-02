# Python Assignment 23

## Python Programming

### Problem 1: Demo Class
Write a Python program to implement a class named `Demo` with the following specifications:
- The class should contain two instance variables: `no1` and `no2`.
- The class should contain one class variable named `Value`.
- Define a constructor (`__init__`) that accepts two parameters and initializes the instance variables.
- Implement two instance methods:
    - `Fun()` - displays the values of instance variables `no1` and `no2`.
    - `Gun()` - displays the values of instance variables `no1` and `no2`.

**Create two objects of the Demo class as follows:**
```python
Obj1 = Demo(11, 21)
Obj2 = Demo(51, 101)
```

**Call the instance methods in the given sequence:**
```python
Obj1.Fun()
Obj2.Fun()
Obj1.Gun()
Obj2.Gun()
```

---

### Problem 2: Circle Class
Write a Python program to implement a class named `Circle` with the following requirements:
- The class should contain three instance variables: `Radius`, `Area`, and `Circumference`.
- The class should contain one class variable named `PI`, initialized to `3.14`.
- Define a constructor (`__init__`) that initializes all instance variables to `0.0`.
- Implement the following instance methods:
    - `Accept()` - accepts the radius of the circle from the user.
    - `CalculateArea()` - calculates the area of the circle and stores it in the `Area` variable.
    - `CalculateCircumference()` - calculates the circumference of the circle and stores it in the `Circumference` variable.
    - `Display()` - displays the values of `Radius`, `Area`, and `Circumference`.
- Create multiple objects of the `Circle` class and invoke all the instance methods for each object.

**Output:**
```
Enter the radius: 4
Radius of Circle is: 4.0
Area of Circle is: 50.24
Circumference of Circle is: 25.12

Enter the radius: 4.3
Radius of Circle is: 4.3
Area of Circle is: 58.0586
Circumference of Circle is: 27.004
```

---

### Problem 3: Arithmetic Class
Write a Python program to implement a class named `Arithmetic` with the following characteristics:
- The class should contain two instance variables: `Value1` and `Value2`.
- Define a constructor (`__init__`) that initializes all instance variables to `0`.
- Implement the following instance methods:
    - `Accept()` - accepts values for `Value1` and `Value2` from the user.
    - `Addition()` - returns the addition of `Value1` and `Value2`.
    - `Subtraction()` - returns the subtraction of `Value1` and `Value2`.
    - `Multiplication()` - returns the multiplication of `Value1` and `Value2`.
    - `Division()` - returns the division of `Value1` and `Value2` (handle division by zero properly).
- Create multiple objects of the `Arithmetic` class and invoke all the instance methods.

**Output:**
```
Enter value1: 6
Enter value2: 4
Addition is: 10.0
Multiplication is: 24.0
Subtraction is: 2.0
Division is: 1.5
```