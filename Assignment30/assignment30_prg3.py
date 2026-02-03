"""
Question:
Display File Line by Line
Problem Statement:
Write a program which accepts a file name from the user and displays the contents of the file line by line on the screen.
Input:
Demo. txt
Expected Output:
Display each line of Demo. txt one by one.

"""

import os
import sys

def displayLinesFromFile(fileName):
    if os.path.exists(fileName) == False:
        print(f"{fileName} does not exist")
        return
    
    fileObj = open(fileName, "r")
    for line in fileObj:
        print(line)
    

def main():
   if len(sys.argv) != 2:
        print("Please provide file name as argument")
        return
   
   fileName = sys.argv[1]
   displayLinesFromFile(fileName)
   
if __name__ == "__main__":
    main()