"""
Question: 
Design a Python application that creates two threads named Prime and NonPrime.
    • Both threads should accept a list of integers.
    • The Prime thread should display all prime numbers from the list.
    • The NonPrime thread should display all non-prime numbers from the list.

"""
import threading

def isNumberPrime(number):
    if number <= 1:
        return False
    if number == 2 or number == 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False
    i = 5
    while i * i <= number:  
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True

getPrimeNumbers = lambda number : isNumberPrime(number)
getNonPrimeNumbers = lambda number : not isNumberPrime(number)

def displayPrime(listData):  
   print(list(filter(getPrimeNumbers, listData)))

def displayNonPrime(listData):
   print(list(filter(getNonPrimeNumbers, listData)))

def main():
   listData = [12, 13, 17, 19, 22, 24, 29, 31, 37, 40, 41, 43]
   primeThream = threading.Thread(target= displayPrime, args=(listData,))
   primeThream.start()

   nonPrimeThream = threading.Thread(target= displayNonPrime, args=(listData,))
   nonPrimeThream.start()


if __name__ == "__main__":
    main()