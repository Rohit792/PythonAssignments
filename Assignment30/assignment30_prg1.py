"""
Question:
Count Lines in a File
Problem Statement:
Write a program which accepts a file name from the user and counts how many lines are present in the file.
Input:
Demo.txt
Expected Output:
Total number of lines in Demo. txt.

"""

import os
import sys

def getTotalNumberOfLines(fileName):
    if os.path.exists(fileName) == False:
        print(f"{fileName} does not exist")
        return
    
    fileObj = open(fileName, "rb")

    lineCount = 0
    for line in fileObj:
        lineCount += 1
    
    return lineCount

def main():
    if len(sys.argv) != 2:
        print("Please provide file name as argument")
        return
   
    fileName = sys.argv[1]
    print(f"{fileName} contains total {getTotalNumberOfLines(fileName)} number of line.")
   
if __name__ == "__main__":
    main()