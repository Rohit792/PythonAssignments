"""
Question: 
Design a Python application that creates two threads.
    • Thread 1 should compute the sum of elements from a list.
    • Thread 2 should compute the product of elements from the same list.
    • Return the results to the main thread and display them.

listData: [1,2,3,4,5]
Sum of elements is: 15
Product of elements 120
"""
import threading
from functools import reduce

getSum = lambda number1, number2: number1 + number2
getProoductOfAllElement = lambda number1, number2: number1 * number2


def getSumOfNumbers(listData, result, index):
    result[index] = reduce(getSum, listData)

def getProductOfNumbers(listData, result, index):
    result[index] = reduce(getProoductOfAllElement, listData)

def main():
   results = [None, None]
   listData = [1,2,3,4,5]
   thread1 = threading.Thread(target=getSumOfNumbers, args=(listData, results, 0))
   thread2 = threading.Thread(target=getProductOfNumbers, args=(listData, results, 1))

    # Start the threads
   thread1.start()
   thread2.start()

   thread1.join()
   thread2.join()

   print("Sum of elements is:", results[0])
   print("Product of elements", results[1])


if __name__ == "__main__":
    main()