"""
Question: Write a program which accept number from user and check whether that number is positive or negative or zero.
Input : 11
Output : Positive Number

Input : -8
Output : Negative Number

Input : 0
Output : Zero

"""

def ChkNum(number):
    if number > 0:
        print("Positive Number")
    elif number < 0:
        print("Negative Number")
    else:
        print("Zero")


def main():
    number = int(input("Enter number: "))
    ChkNum(number)

if __name__ == "__main__":
    main()