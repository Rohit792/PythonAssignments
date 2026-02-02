"""
Question:
Write a Python program to implement a class named Demo with the following specifications:
• The class should contain two instance variables: no 1 and no 2.
• The class should contain one class variable named Value.
• Define a constructor (__init) that accepts two parameters and initializes the instance variables.
• Implement two instance methods:
    • Fun () - displays the values of instance variables no 1 and no2.
    • Gun () - displays the values of instance variables no1 and no2.

Create two objects of the Demo class as follows:
Objl = Demo (11, 21)
Obj2 = Demo (51, 101)

Call the instance in given sequance:
Obj1.Fun()

Obj2. Fun()
Objl.Gun()
Obj2. Gun()

"""

class Demo:
    def __init__(self, no1, no2):
        self.value1 = no1
        self.value2 = no2

    def Fun(self):
        print("Value1: ", self.value1)
        print("Value2: ", self.value2)


    def Gun (self):
        print("Value1: ", self.value1)
        print("Value2: ", self.value2)

if __name__ == "__main__":
    Objl = Demo(11, 21)
    Obj2 = Demo(51, 101)

    Objl.Fun()
    Obj2.Fun()
    Objl.Gun()
    Obj2.Gun()
