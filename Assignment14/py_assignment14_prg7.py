"""
Question: Write a lambda function which accepts one number and returns True if divisible by 5.

Enter Number: 55
Is Number Divisible by 5:  True

Enter Number: 4
Is Number Divisible by 5:  False

"""

isDivisibleByFive = lambda number: True if (number % 5 == 0) else False

def main():
    number = int(input("Enter Number: "))

    print("Is Number Divisible by 5: ", isDivisibleByFive(number))

if __name__ == "__main__":
    main()