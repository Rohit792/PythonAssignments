"""
Question:
Write a Python program to implement a class named Arithmetic with the following characteristics:
• The class should contain two instance variables: Value1 and Value2.
• Define a constructor() init() that initializes all instance variables to 0.
• Implement the following instance methods:
    • Accept() - accepts values for Valuel and Value2 from the user.
    • Addition() - returns the addition of Valuel and Value2.
    • Subtraction() - returns the subtraction of Valuel and Value2.
    • Multiplication() - returns the multiplication of Valuel and Value2.
    • Division() - returns the division of Valuel and Value2 (handle division by zero properly).
• Create multiple objects of the Arithmetic class and invoke all the instance methods.

Output:
Enter value1: 6
Enter value2: 4
Addition is:  10.0
Multiplication is:  24.0
Substraction is:  2.0
Division is:  1.5

"""

class Arithmetic:
    def __init__(self):
        self.Value1 = 0
        self.Value2 = 0

    def Accept(self):
        self.Value1 = float(input("Enter value1: "))
        self.Value2 = float(input("Enter value2: "))

    def Addition(self):
        return self.Value1 + self.Value2

    def Subtraction(self):
        return self.Value1 - self.Value2
    
    def Multiplication(self):
        return self.Value1 * self.Value2
 
    def Division(self):
      if self.Value1 > 0 and self.Value2 > 0:
          return self.Value1 / self.Value2
      print("Make sure that values are greater than Zero")
      return 0

if __name__ == "__main__":
    Objl = Arithmetic()
    Obj2 = Arithmetic()

    Objl.Accept()
    print("Addition is: ", Objl.Addition())
    print("Multiplication is: ", Objl.Multiplication())
    print("Substraction is: ", Objl.Subtraction())
    print("Division is: ", Objl.Division())

