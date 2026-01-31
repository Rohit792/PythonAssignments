"""
Question: Write a program which accept one number and display below pattern.
Input : 5
Output :
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5

"""

 
def displayPatern(number):
    for i in range(number):
        print(*range(1,i+2))

def main():
    number = int(input("Enter number: "))
    displayPatern(number)

if __name__ == "__main__":
    main()

    