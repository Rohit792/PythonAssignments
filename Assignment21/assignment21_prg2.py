"""
Question: 
Design a Python application that creates two threads.
    • Thread 1 should calculate and display the maximum element from an list.
    • Thread 2 should calculate and display the minimum element from the same list.
    • The list should be accepted from the user.

"""
import threading
from functools import reduce

getMaxNumber = lambda number1, number2: number1 if number1 > number2 else number2
getMinNumber = lambda number1, number2: number1 if number1 < number2 else number2

def displauMaxNumber(listData):  
   print("\nMaximun number is: ", reduce(getMaxNumber, listData))

def displayMinNumber(listData):
   print("Minimum number is: ", reduce(getMinNumber, listData))

def main():
   number = int(input("Enter number of elements: "))
   listData = []

   for i in range(number):
      listData.append(int(input(f"Enter element at {i}: ")))

   primeThream = threading.Thread(target= displauMaxNumber, args=(listData,))
   primeThream.start()

   nonPrimeThream = threading.Thread(target= displayMinNumber, args=(listData,))
   nonPrimeThream.start()


if __name__ == "__main__":
    main()