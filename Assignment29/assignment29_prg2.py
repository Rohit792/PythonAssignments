"""
Question:
Display File Contents

Problem Statement:
console.
Write a program which accepts a file name from the user, opens that file, and displays the entire contents on the

"""

def displayFileData(fileName = "demo.txt"):
    fobj = open(fileName, "r")
    print(fobj.read())
    fobj.close()

def main():
   fileName = input("Enter file name: ")
   displayFileData(fileName) 

if __name__ == "__main__":
    main()