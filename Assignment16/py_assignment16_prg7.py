"""
Question: Write a program which contains one function that accept one number from user and returns true if number is divisible by 5 otherwise return false.
Input : 8
Output : False
Input : 25
Output : True

"""

def isNumDivideByFive(number):
    return number % 5 == 0


def main():
    number = int(input("Enter number: "))
    print(isNumDivideByFive(number))

if __name__ == "__main__":
    main()