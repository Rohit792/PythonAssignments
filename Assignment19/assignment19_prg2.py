"""
Question: Write a program which contains one lambda function which accepts two parameters and return its multiplication.
Enter a number first: 4
Enter a number second: 3
Multiplication of 4 & 3 is 12

Enter a number first: 6
Enter a number second: 3
Multiplication of 6 & 3 is 18
"""

multiPlication = lambda number1, number2: number1 * number2

def main():
    number1 = int(input("Enter a number first: "))
    number2 = int(input("Enter a number second: "))

    result = multiPlication(number1, number2)
    print(f"Multiplication of {number1} & {number2} is {result}")

if __name__ == "__main__":
    main()