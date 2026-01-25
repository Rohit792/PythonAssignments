"""
Question: Write a lambda function using reduce () which accepts a list of numbers and returns the maximum element.

Maximum of [1, 12, 3, 4] is 12

"""
from functools import reduce

getMaximumNumber = lambda number1, number2: number1 if number1 > number2 else number2

def main():
    listData = [1, 12, 3, 4]
    print(f" Maximum of {listData} is", reduce(getMaximumNumber,listData))

if __name__ == "__main__":
    main()