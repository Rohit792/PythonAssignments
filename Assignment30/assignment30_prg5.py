"""
Question:
Search a Word in File
Problem Statement:
Write a program which accepts a file name and a word from the user and checks whether that word is present in the file or not.
Input:
Demo.txt Marvellous
Expected Output:
Display whether the word Marvellous is found in Demo. txt or not.

"""


import sys
import os
def findWordInFile(fileName, searchKeyWord):
    if os.path.exists(fileName) == False:
        print(f"{fileName} does not exist")
        return
    keyword_bytes = searchKeyWord.encode('utf-8')
    fileObj = open(fileName, "rb")
    isWordFound = False

    for line in fileObj:
        if line.count(keyword_bytes) > 0:
            isWordFound = True
            break

    if isWordFound == True:
        print(f"Word {searchKeyWord} is found in {fileName}")
    else:
        print(f"Word {searchKeyWord} is not found in {fileName}")

def main():
   
    if len(sys.argv) != 3:
        print("Please provide file name and searchKeyWord as argument")
        return
    
    fileName = sys.argv[1]
    searchKeyWord = sys.argv[2]
    findWordInFile(fileName, searchKeyWord)
   
if __name__ == "__main__":
    main()