"""
Question:
Check File Exists in Current Directory
Problem Statement:
Write a program which accepts a file name from the user and checks whether that file exists in the current directory or not.

output:
Enter file name: demo.txt
demo.txt exist

Enter file name: hello.txt
hello.txt does not exist
"""

import os

def checkIfFileExist(fileName = "demo.txt"):
    return os.path.exists(fileName)

def main():
   fileName = input("Enter file name: ")
   print(f"{fileName} exist") if checkIfFileExist(fileName) else print(f"{fileName} does not exist")

if __name__ == "__main__":
    main()