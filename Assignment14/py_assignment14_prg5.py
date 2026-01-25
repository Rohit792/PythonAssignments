"""
Question: Write a lambda function which accepts one number and returns True if number is even otherwise False.

Enter Number: 4
Is Number Even:  True

Enter Number: 3
Is Number Even:  False

"""

isNumberEven = lambda number: True if (number % 2 == 0) else False

def main():
    number = int(input("Enter Number: "))

    print("Is Number Even: ", isNumberEven(number))

if __name__ == "__main__":
    main()