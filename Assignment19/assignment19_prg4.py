"""
Question: Write a program which contains filter(), map() and reduce in it. 
Python application which contains one list of numbers. 
1. List contains the numbers which are accepted from user. 
2. Filter should filter out all such numbers which are even. 
3. Map function will calculate its square.
4. Reduce will return addition of all that numbers.
Input List = [5, 2, 3, 4, 3, 4, 1, 2, 8, 10]
List after filter = [2, 4, 4, 2, 8, 10]
List after map = [4, 16, 16, 4, 64, 100]
Output of reduce = 204

"""
from functools import reduce

getEvenNumber = lambda number: number % 2 == 0
getSquareOfNumber = lambda number: number ** 2
getAdditionOfNumbers = lambda number1, number2: number1 + number2

def main():
    
    number = int(input("Enter number of elements: "))
    listData = []

    for i in range(number):
        listData.append(int(input(f"Enter element at index {i}: ")))

    filterValue = list(filter(getEvenNumber, listData))
    mapValue = list(map(getSquareOfNumber, filterValue))
    productOfAllElement = reduce(getAdditionOfNumbers, mapValue)

    print(f"List after filter = {filterValue}\nList after map = {mapValue}\nOutput of reduce = {productOfAllElement}")

if __name__ == "__main__":
    main()