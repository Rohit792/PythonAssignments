"""
Question: Write a lambda function which accepts one number and returns True if number is odd otherwise False.

Enter Number: 2
Is Number Odd:  False

Enter Number: 3
Is Number Odd:  True

"""

isNumberOdd = lambda number: True if (number % 2 != 0) else False

def main():
    number = int(input("Enter Number: "))

    print("Is Number Odd: ", isNumberOdd(number))

if __name__ == "__main__":
    main()