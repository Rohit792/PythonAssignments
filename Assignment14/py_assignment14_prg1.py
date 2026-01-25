"""
Question: Write a lambda function which accepts one number and returns square of that number.
Enter Number: 4
Square of 4 is:  16

"""

getSquareOf = lambda number: number ** 2

def main():
    number = int(input("Enter length: "))
    print(f"Square of {number} is: ", getSquareOf(number))

if __name__ == "__main__":
    main()