"""
Question: Write a program which accept number from user and return addition of digits in that number.
Input : 5187934
Output : 37

"""

 
def getTotalOfDigitsFrom(number):
    no = number
    totalOfDigits = 0

    while no != 0:
        totalOfDigits += (no % 10)
        no = int(no / 10)

    return totalOfDigits


def main():
    number = int(input("Enter number: "))
    print(f"Total of digits in {number} is {getTotalOfDigitsFrom(number)}")

if __name__ == "__main__":
    main()

    