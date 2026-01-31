"""
Question: Write a program which accept one number and display below pattern.
Enter number: 5
* * * * * 
* * * * * 
* * * * * 
* * * * * 
* * * * * 

"""
 
def main():
    number = int(input("Enter number: "))

    for i in range(number):
        print("* "*number)

if __name__ == "__main__":
    main()