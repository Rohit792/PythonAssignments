"""
Question: Write a program which accept number from user and print that number of *" on screen.
Input : 5
Output : * * * * * 

"""

def displayStars(number):
    print("* "*number)


def main():
    number = int(input("Enter number: "))
    print(displayStars(number))

if __name__ == "__main__":
    main()