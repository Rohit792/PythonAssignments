"""
Question: Write a lambda function which accepts two numbers and returns maximum number.
Enter Number1: 21
Enter Number2: 101
Maximum number is:  101

Condition Referece: https://peps.python.org/pep-0308/
"""

getMaximumFrom = lambda number1, number2: number1 if number1 > number2 else number2

def main():
    number1 = int(input("Enter Number1: "))
    number2 = int(input("Enter Number2: "))

    print("Maximum number is: ", getMaximumFrom(number1, number2))

if __name__ == "__main__":
    main()