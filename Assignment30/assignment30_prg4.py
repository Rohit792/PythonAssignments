"""
Question:
Copy File Contents into Another File
Problem Statement:
Write a program which accepts two file names from the user.
• First file is an existing file
• Second file is a new file
Copy all contents from the first file into the second file.

Input:
ABC.txt Demo.txt
Expected Output:
Contents of ABC. txt copied into Demo. txt.

"""


import sys
import os

def copyFileIntoNew(fileName, newFileName):
    
    if os.path.exists(fileName) == False:
        print("File does not found")
        return

    fobj = open(fileName, "r")
    fileData = fobj.read()

    copyFObj = open(newFileName, "w")
    copyFObj.write(fileData)

    print(f"Contents of {fileName} copied into {newFileName}")
    copyFObj.close()
    fobj.close()

def main():
    if len(sys.argv) != 3:
       print("Please provide file name as argument.")
       return
    
    copyFileIntoNew(sys.argv[1], sys.argv[2]) 

if __name__ == "__main__":
    main()