"""
Question: Create on module named as Arithmetic which contains 4 functions as 
Add() for addition, 
Sub() for subtraction, 
Mult() for multiplication
Div() for division. 
All functions accepts two parameters as number and perform the operation. 
Write on python program which call all the functions from Arithmetic module by accepting the parameters from user.

Enter first number: 21
Enter second number: 11
21 + 11 = 32
21 - 11 = 10
21 * 11 = 231
21 / 11 = 1.9090909090909092

"""
import Arithmetic as math
 
def main():
    number1 = int(input("Enter first number: "))
    number2 = int(input("Enter second number: "))

    print(f"{number1} + {number2} = {math.Add(number1, number2)}")
    print(f"{number1} - {number2} = {math.Sub(number1, number2)}")
    print(f"{number1} * {number2} = {math.Mult(number1, number2)}")
    print(f"{number1} / {number2} = {math.Div(number1, number2)}")

if __name__ == "__main__":
    main()