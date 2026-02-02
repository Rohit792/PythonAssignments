"""
Question:
Write a Python program to implement a class named Circle with the following requirements:
    • The class should contain three instance variables: Radius, Area, and Circumference.
    • The class should contain one class variable named PI, initialized to 3.14.
    • Define a constructor (_init_) that initializes all instance variables to O. O.
    • Implement the following instance methods:
        • Accept () - accepts the radius of the circle from the user.
        • CalculateArea () - calculates the area of the circle and stores it in the Area variable.
        • CalculateCircumference () - calculates the circumference of the circle and stores it in the Circumference variable.
        • Display () - displays the values of Radius, Area, and Circumference.
    • Create multiple objects of the Circle class and invoke all the instance methods for each object.

Enter the radious: 4
Radius of Circle is:  4.0
Area of Circle is:  50.24
Circumference of Circle is:  25.12

Enter the radious: 4.3
Radius of Circle is:  4.3
Area of Circle is:  58.0586
Circumference of Circle is:  27.004
"""

class Circle:
    def __init__(self):
        self.radius = 0
        self.area = 0
        self.circumference = 0
        self.PI = 3.14

    def Accept(self):
        self.radius = float(input("Enter the radious: "))
        print("Radius of Circle is: ", self.radius)

    def CalculateArea(self):
        self.area = self.PI * (self.radius ** 2)
        print("Area of Circle is: ", self.area)

 
    def CalculateCircumference(self):
       self.circumference = 2 * self.PI * self.radius
       print("Circumference of Circle is: ", self.circumference)

    def Display(self):
       self.Accept()
       self.CalculateArea()
       self.CalculateCircumference()

if __name__ == "__main__":
    Objl = Circle()
    Obj2 = Circle()

    Objl.Display()
    Obj2.Display()
     