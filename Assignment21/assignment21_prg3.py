"""
Question: 
Design a Python application where multiple threads update a shared variable.
    • Use a Lock to avoid race conditions.
    • Each thread should increment the shared counter multiple times.
    • Display the final value of the counter after all threads complete execution.

"""
import threading
from functools import reduce

number = 0
lobj = threading.Lock()

def increaseNumber():  
  global number
  for _ in range(100000):
        with lobj: 
         number = number + 1


def main():
   global number
   thread1 = threading.Thread(target= increaseNumber)
   thread2 = threading.Thread(target= increaseNumber)

   thread1.start()
   thread2.start()

   thread1.join()
   thread2.join()
   print("Value of number is: ", number)


if __name__ == "__main__":
    main()