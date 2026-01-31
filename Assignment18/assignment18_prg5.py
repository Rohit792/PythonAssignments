"""
Question: Write a program which accept N numbers from user and store it into List. 
Return addition of all prime numbers from that List. 
Main python file accepts N numbers from user and pass each number to ChkPrime() function which is part of our user defined module named as MarvellousNum. 
Name of the function from main python file should be ListPrime().

Input : 
Number of elements : 11
Input Elements : 13 5 45 7 4 56 10 34 2 5 8
Output : 32 (13 + 5 + 7 + 2 + 5)


"""
import MarvellousNum as checkPrime

def ListPrime(listData):
    sumOfPrime = 0

    for i in range(len(listData)):        
        if checkPrime.isNumberPrime(listData[i]):
            print(listData[i])
            sumOfPrime += listData[i]

    return sumOfPrime

def main():
    number = int(input("Enter number of elements: "))
    listData = []

    for i in range(number):
        listData.append(int(input(f"Please enter elemnt at index {i}: ")))
    
    print("Prime number count is: ", ListPrime(listData))

if __name__ == "__main__":
    main()