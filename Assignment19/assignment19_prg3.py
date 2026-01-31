"""
Question: Write a program which contains filter(), map() and reduce() in it. 
Python application which contains one list of numbers. 
List contains the numbers which are accepted from user. 
1. Filter should filter out all such numbers which greater than or equal to 70 and less than or equal to 90.
2. Map function will increase each number by 10. 
3. Reduce will return product of all that numbers.


Input List = [4, 34, 36, 76, 68, 24, 89, 23, 86, 90, 45, 70]
List after filter = [76, 89, 86, 90, 70]
List after map = [86, 99, 96, 100, 80]
Output of reduce = 6538752000
"""
from functools import reduce

getFiletedNumber = lambda number: number  >= 70 and number <= 90
increaseNumberBy10 = lambda number: number + 10
getProoductOfAllElement = lambda number1, number2: number1 * number2

def main():
    listData = [4, 34, 36, 76, 68, 24, 89, 23, 86, 90, 45, 70]


    filterValue = list(filter(getFiletedNumber, listData))
    mapValue = list(map(increaseNumberBy10, filterValue))
    productOfAllElement = reduce(getProoductOfAllElement, mapValue)

    print(f"List after filter = {filterValue}\nList after map = {mapValue}\nOutput of reduce = {productOfAllElement}")

if __name__ == "__main__":
    main()