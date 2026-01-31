"""
Question: 
Design a Python application that creates two separate threads named Even and Odd.
• The Even thread should display the first 10 even numbers.
• The Odd thread should display the first 10 odd numbers.
• Both threads should execute independently using the threading module.
• Ensure proper thread creation and execution.

"""
import threading

def getFirstTenEvenNUmber():
    evenCount = 0
    i = 0

    print("Even numbers are: ")
    while evenCount != 10:
        if i % 2 == 0:
            print(i)
            evenCount += 1
        i += 1

def getFirstTenOddNUmber():
    evenCount = 0
    i = 0

    print("Odd numbers are: ")
    while evenCount != 10:
        if i % 2 != 0:
            print(i)
            evenCount += 1
        i += 1

def main():
   evenThread = threading.Thread(target= getFirstTenEvenNUmber)
   evenThread.start()

   oddThread = threading.Thread(target= getFirstTenOddNUmber)
   oddThread.start()


if __name__ == "__main__":
    main()