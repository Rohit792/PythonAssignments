"""
Question: Write a lambda function using reduce () which accepts a list of numbers and returns the product of all elements.
 
Enter number of elements: 
5
Enter number 1: 1
Enter number 2: 2
Enter number 3: 3
Enter number 4: 4
Enter number 5: 5
List of elements are: 
 [1, 2, 3, 4, 5]

Product of all elements: 120

"""
from functools import reduce

getProoductOfAllElement = lambda number1, number2: number1 * number2

def main():
    print("Enter number of elements: ")
    numberOfElements = int(input())
    listData = []

    for i in range(numberOfElements):
        listData.append(int(input(f"Enter number {i + 1}: ")))

    print(f"List of elements are: \n {listData}\n")
    print(f"Product of all elements: { reduce(getProoductOfAllElement, listData)}")

if __name__ == "__main__":
    main()