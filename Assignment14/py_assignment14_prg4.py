"""
Question: Write a lambda function which accepts two numbers and returns minimum number.

Enter Number1: 22
Enter Number2: 33

Minimum number is:  22

"""

getMinimumFrom = lambda number1, number2: number1 if number1 < number2 else number2

def main():
    number1 = int(input("Enter Number1: "))
    number2 = int(input("Enter Number2: "))

    print("Minimum number is: ", getMinimumFrom(number1, number2))

if __name__ == "__main__":
    main()