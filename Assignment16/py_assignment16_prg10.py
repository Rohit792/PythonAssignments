"""
Question: WWrite a program which accept name from user and display length of its name.
Input : Marvellous
Output : 10

"""

def displayLengthOfName(name):
    print(len(name))

def main():
    name = input("Enter Name: ")
    displayLengthOfName(name)

if __name__ == "__main__":
    main()