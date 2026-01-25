"""
Question: Write a lambda function using filter () which accepts a list of numbers and returns a list of odd numbers.

List of odd number from [1, 2, 3, 4] is [1, 3]
"""

isOddNumber = lambda number:( number % 2 != 0)

def main():
    listData = [1, 2, 3, 4]
    print(f" List of odd number from {listData} is", list(filter(isOddNumber, listData)))

if __name__ == "__main__":
    main()