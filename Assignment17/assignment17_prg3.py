"""
Question: Write a program which accept one number from user and return its factorial.
Input : 5
Output : 120

"""

def displayFactorialOf(number):
    
    factorial = number
    for i in range(number, 1, -1):
        factorial = factorial * (i - 1)
    print(factorial)
 
def main():
    number = int(input("Enter number: "))
    displayFactorialOf(number = number)

if __name__ == "__main__":
    main()