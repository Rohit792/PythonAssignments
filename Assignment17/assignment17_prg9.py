"""
Question: Write a program which accept number from user and return number of digits in that number
Input : 5187934
output: 7

"""

 
def getNumberOfDigitsFrom(number):
    no = number
    digitCounter = 0

    while no != 0:
        no = int(no / 10)
        digitCounter += 1

    return digitCounter


def main():
    number = int(input("Enter number: "))
    print(f"Number of digits in {number} is {getNumberOfDigitsFrom(number)}")

if __name__ == "__main__":
    main()

    