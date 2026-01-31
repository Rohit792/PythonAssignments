"""
Question:
Design a Python application that creates two threads named EvenList and OddList.
• Both threads should accept a list of integers as input.
• The EvenList thread should:
   • Extract all even elements from the list.
   • Calculate and display their sum.
• The OddList thread should:
    • Extract all odd elements from the list.
    • Calculate and display their sum.
• Threads should run concurrently.


Actual list is:  [1, 2, 3, 4, 5, 6]

The Even element List is:  [2, 4, 6]
The sum of even list is:  12

Odd factors 
The odd Element List is:  [1, 3, 5]
The sum of odd element is:  9

"""
import threading
from functools import reduce
 
addNumbers = lambda number1, number2: number1 + number2

def EvenList(listData):
    
    evenElementList = []
    for i in range(len(listData)):
        if listData[i] % 2 == 0:
            evenElementList.append(listData[i])

    print("The Even element List is: ", evenElementList)
    print("The sum of even list is: ",reduce(addNumbers, evenElementList))

def OddList(listData):
    
    oddElementList = []
    print("Odd factors ")
    for i in range(len(listData)):
        if (listData[i] % 2 != 0):
            oddElementList.append(listData[i])

    print("The odd Element List is: ", oddElementList)
    print("The sum of odd element is: ",reduce(addNumbers, oddElementList))

def main():
   listData = [1,2,3,4,5,6]
   print("Actual list is: ", listData)
   evenThread = threading.Thread(target= EvenList, args=(listData,))
   evenThread.start()

   oddThread = threading.Thread(target= OddList, args=(listData,))
   oddThread.start()
   
if __name__ == "__main__":
    main()