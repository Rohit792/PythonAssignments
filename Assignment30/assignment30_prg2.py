"""
Question:
Count Words in a File
Problem Statement:
Write a program which accepts a file name from the user and counts the total number of words in that file.

Input:
Demo.txt/
Expected Output:
Total number of words in Demo.txt.

"""

import os
import sys

def getTotalNumberOfWordsFrom(fileName):
    if os.path.exists(fileName) == False:
        print(f"{fileName} does not exist")
        return
    
    fileObj = open(fileName, "rb")
    wordCount = 0
    for line in fileObj:
        wordCount += len((str(line)).split(" "))
    
    return wordCount

def main():
   
    if len(sys.argv) != 2:
        print("Please provide file name as argument")
        return
   
    fileName = sys.argv[1]
    print(f"{fileName} contains total {getTotalNumberOfWordsFrom(fileName)} number of words.")
   
if __name__ == "__main__":
    main()