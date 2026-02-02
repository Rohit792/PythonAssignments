"""
Question:
1: Write a Python program to implement a class named Numbers with the following specifications:
• The class should contain one instance variable:
   • Value
• Define a constructor (__init__) that accepts a number from the user and initializes Value.
• Implement the following instance methods:
   • ChkPrime () - returns True if the number is prime, otherwise returns False
   • ChkPerfect () - returns True if the number is perfect, otherwise returns False
   • Factors () - displays all factors of the number
   • SumFactors () - returns the sum of all factors
    (You may use this method as a helper inChkPerfect() if required)
• Create multiple objects and call all


Enter number: 6
6 is not a prime
6 is a Perfect Number
Factors are:  1 2 3 6
Factors are:  1 2 3 6
Sum of factors is:  12

"""
from functools import reduce

class Numbers:

    def __init__(self, number):
        self.Value = number


    def ChkPrime(self):
        if self.isNumberPrime(self.Value) == True:
           print(f"{self.Value} is a Prime")
        else:
            print(f"{self.Value} is not a prime")


    def ChkPerfect(self):
        if self.isPerfect(self.Value) == True:
           print(f"{self.Value} is a Perfect Number")
        else:
            print(f"{self.Value} is not a Perfect Number.")

    def Factors(self):
        factors = []
        for i in range(1, self.Value + 1):
            if self.Value % i == 0:
                factors.append(i)
   
        print("Factors are: ", * factors)
        return factors

    def SumFactors(self):
        factors = self.Factors()
        sumFactors = reduce(lambda number1, number2: number1 + number2, factors)

        print("Sum of factors is: ", sumFactors)

    
    def isPerfect(self, number):
        sum = 0
        for i in range(1, number):
            if number % i == 0:
                sum += i
        return sum == number
                
    def isNumberPrime(self, number):
        if number <= 1:
            return False
        if number == 2 or number == 3:
            return True
        if number % 2 == 0 or number % 3 == 0:
            return False
        i = 5
        while i * i <= number:  
            if number % i == 0 or number % (i + 2) == 0:
                return False
            i += 6
        return True
 
if __name__ == "__main__":
    number = int(input("Enter number: "))
    Obj1 = Numbers(number)
    Obj1. ChkPrime()
    Obj1.ChkPerfect() 
    Obj1.Factors()
    Obj1.SumFactors()
     
 

     
