"""
Question: Write a lambda function which accepts two numbers and returns addition.

Enter Number1: 5
Enter Number2: 4
Addition of 5 + 4 is  9

"""

getAdditionOf = lambda number1, number2: number1 + number2

def main():
    number1 = int(input("Enter Number1: "))
    number2 = int(input("Enter Number2: "))

    print(f"Addition of {number1} + {number2} is ", getAdditionOf(number1, number2))

if __name__ == "__main__":
    main()