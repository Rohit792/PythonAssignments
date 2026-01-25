"""
Question: Write a lambda function using filter () which accepts a list of numbers and returns the count of even numbers.

"""
from functools import reduce

getAllEvenNumberFromList = lambda number: number % 2 == 0
addContOfEvenNUmber = lambda number: number + 1

def main():
    print("Enter number of elements: ")
    numberOfElements = int(input())
    listData = []

    for i in range(numberOfElements):
        listData.append(int(input(f"Enter number {i + 1}: ")))

    print(f"List of elements are: \n {listData}\n")
    print("Count of: ", len(list(filter(getAllEvenNumberFromList, listData))))

if __name__ == "__main__":
    main()