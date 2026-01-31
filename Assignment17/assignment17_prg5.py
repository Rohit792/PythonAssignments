"""
Question: Write a program which accept one number for user and check whether number is prime or not.
Input: 5
Output : It is Prime Number

"""

 
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

def main():
    number = int(input("Enter number: "))
    print(f"It is {"Prime Number" if isNumberPrime(number) == True else "not Prime Number"}")

if __name__ == "__main__":
    main()