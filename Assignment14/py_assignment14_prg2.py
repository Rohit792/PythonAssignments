"""
Question: Write a lambda function which accepts one number and returns cube of that number.
Enter Number: 3
Cube of 3 is:  27

"""

getCubeeOf = lambda number: number ** 3

def main():
    number = int(input("Enter Number: "))
    print(f"Cube of {number} is: ", getCubeeOf(number))

if __name__ == "__main__":
    main()