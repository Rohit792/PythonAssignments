"""
Question: Write a program which contains filter(), map() and reduce() in it. 
Python application which contains one list of numbers. 
List contains the numbers which are accepted from user. 
Filter should filter out all prime numbers. 
Map function will multiply each number by 2. 
Reduce will return Maximum number from that numbers. 
(You can also use normal functions instead of lambda functions).

Input List = [2, 70 , 11, 10, 17, 23, 31, 77]
List after filter = [2, 11, 17, 23, 31]
List after map = [4, 22, 34, 46, 62]
Output of reduce = 62

"""
from functools import reduce


def isNumberPrime(number):
    if number <= 1:
        return False
    if number == 2 or number == 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False
    i = 5
    while i * i <= number:  
        print(i)
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True

getPrimeNumber = lambda number: isNumberPrime(number)
getMultipleOfTwo = lambda number: number * 2
getMaximumNumber = lambda number1, number2: number1 if number1 > number2 else number2

def main():
    
    number = int(input("Enter number of elements: "))
    listData = []
    for i in range(number):
        listData.append(int(input(f"Enter element at index {i}: ")))

    filterValue = list(filter(getPrimeNumber, listData))
    mapValue = list(map(getMultipleOfTwo, filterValue))
    productOfAllElement = reduce(getMaximumNumber, mapValue)

    print("Input List = ", listData)
    print(f"List after filter = {filterValue}\nList after map = {mapValue}\nOutput of reduce = {productOfAllElement}")

if __name__ == "__main__":
    main()