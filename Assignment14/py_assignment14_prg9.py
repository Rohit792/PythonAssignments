"""
Question: Write a lambda function which accepts two numbers and returns multiplication.

Enter Number1: 3
Enter Number2: 3
Multiplication of 3 * 3 is  9

"""

getMultiplcationOf = lambda number1, number2: number1 * number2

def main():
    number1 = int(input("Enter Number1: "))
    number2 = int(input("Enter Number2: "))

    print(f"Multiplication of {number1} * {number2} is ", getMultiplcationOf(number1, number2))

if __name__ == "__main__":
    main()