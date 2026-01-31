"""
Question: Write a program which contains one lambda function which accepts one parameter and return power of two.
Input : 4
Output : 16

Input : 6
Output : 36


"""

powerFun = lambda number: number ** 2

def main():
    number = int(input("Enter a number: "))
    
    result = powerFun(number)
    print(f"The power of two for {number} is {result}")

if __name__ == "__main__":
    main()