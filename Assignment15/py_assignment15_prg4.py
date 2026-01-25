"""
Question: Write a lambda function using reduce () which accepts a list of numbers and returns the addition of all elements.

Adtion of [1, 2, 3, 4] is 10
"""
from functools import reduce

addNumbers = lambda number1, number2: number1 + number2

def main():
    listData = [1, 2, 3, 4]
    print(f" Adtion of {listData} is", reduce(addNumbers,listData))

if __name__ == "__main__":
    main()