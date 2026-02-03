"""
Question:
Copy File Contents into a New File (Command Line)
Problem Statement:
Write a program which accepts an existing file name through command line arguments, creates a new file named Demo. txt, and copies all contents from the given file into Demo. txt.

Input (Command Line):
ABC.txt
Expected Output:
Create Demo.txt and copy contents of ABC.txt into Demo. txt.

"""
import sys
import os

def displayFileData(fileName = "ABC.txt"):
    
    if os.path.exists(fileName) == False:
        print("File does not found")
        return

    fobj = open(fileName, "r")
    fileData = fobj.read()

    copyFileName = "demo.txt"
    copyFObj = open(copyFileName, "w")
    copyFObj.write(fileData)

    print(f"Created {copyFileName} and copy contents of {fileName} into {copyFileName}")
    copyFObj.close()
    fobj.close()

def main():
    if len(sys.argv) != 2:
       print("Please provide file name as argument.")
       return
    
    fileName = sys.argv[1]
    displayFileData(fileName) 

if __name__ == "__main__":
    main()