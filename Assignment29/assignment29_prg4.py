"""
Question:
Compare Two Files (Command Line)
Problem Statement:
Write a program which accepts two file names through command line arguments and compares the contents of both files.
    • If both files contain the same contents, display Success
    • Otherwise display Failure

Input (Command Line):
Demo.txt
Hello.txt
Expected Output:
Success OR Failure


"""
import os
import sys
import hashlib

def calculateCheckSum(fileName):
    fileobj = open(fileName, "rb")
    hashobj = hashlib.md5()

    buffer = fileobj.read(1024)

    while len(buffer) > 0:
        hashobj.update(buffer)
        buffer = fileobj.read(1024)

    fileobj.close()
    return hashobj.hexdigest()

def compareTwoFiles(firstFile, secondFile):

    if os.path.exists(firstFile) == False:
        print(f"{firstFile} does not exists.")
        return
    
    if os.path.exists(secondFile) == False:
        print(f"{secondFile} does not exists.")
        return
    
    firstCheckSum = calculateCheckSum(firstFile)
    secondCheckSum = calculateCheckSum(secondFile)

    if firstCheckSum == secondCheckSum:
        print("Success")
    else:
        print("Failure")

def main():
    if len(sys.argv) != 3:
       print("Please provide 2 file names as argument.")
       return
    
    firstFile = sys.argv[1]
    seconfFile = sys.argv[2]

    compareTwoFiles(firstFile, seconfFile) 

if __name__ == "__main__":
    main()