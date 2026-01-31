"""
Question: Write a program which contains one function named as Add() which accepts two numbers from user and return addition of that two numbers.

Enter first number: 11
Enter second number: 5
Addition of 11 + 5 is 16

"""

def Add(number1, number2):
    return number1 + number2

def main():
    number1 = int(input("Enter first number: "))
    number2 = int(input("Enter second number: "))
    print(f"Addition of {number1} + {number2} is {Add(number1, number2)}")

if __name__ == "__main__":
    main()