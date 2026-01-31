"""
Question:
Design a Python application that creates two threads named EvenFactor and OddFactor.
• Both threads should accept one integer number as a parameter.
• The EvenFactor thread should:
    • Identify all even factors of the given number.
    • Calculate and display the sum of even factors.
• The OddFactor thread should:
    • Identify all odd factors of the given number.
    • Calculate and display the sum of odd factors.
• After both threads complete execution, the main thread should display the message:
"Exit from main"

Enter a number to find its factors: 6
Even factors 
[2, 6]
Odd factors 
[1, 3]
Exit from main

"""
import threading

 
def getEvenFactor(number):
    
    print("Even factors ")
    evenFactorList = []
    for i in range(1, number + 1):
        if (number % i == 0) and (i % 2 == 0):
            evenFactorList.append(i)
    print(evenFactorList)

def getOddFactor(number):
    
    oddFactorList = []
    print("Odd factors ")
    for i in range(1, number + 1):
        if (number % i == 0) and (i % 2 != 0):
            oddFactorList.append(i)
    print(oddFactorList)

def main():
   number = int(input("Enter a number to find its factors: "))
   evenThread = threading.Thread(target= getEvenFactor, args=(6,))
   evenThread.start()

   oddThread = threading.Thread(target= getOddFactor, args=(6,))
   oddThread.start()
   
   evenThread.join()
   oddThread.join()
   print("Exit from main")

if __name__ == "__main__":
    main()