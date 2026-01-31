"""
Question: Write a program which accept one number and display below pattern.
Input : 5
Output :
* * * * * 
* * * * 
* * * 
* * 
* 

"""

 
def displayPatern(number):
    for i in range(number):
        print("* "*(number - i))

def main():
    number = int(input("Enter number: "))
    displayPatern(number)

if __name__ == "__main__":
    main()