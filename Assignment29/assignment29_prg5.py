"""
Question:
Frequency of a String in File
Problem Statement:
Write a program which accepts a file name and one string from the user and returns the frequency (count of occurrences) of that string in the file.

Input:
demo_search.txt Marvellous
The word 'Marvellous' appears 3 times in the demo_search.txt file.

"""
import os
import sys
import hashlib

searchCount = lambda str1, str2: str1 == str2
def searchKeyWordInFile(fileName, keyWordTtSearch):

    if os.path.exists(fileName) == False:
        print(f"{fileName} does not exists.")
        return

    keyword_bytes = keyWordTtSearch.encode('utf-8')
    count = 0
    fileObj = open(fileName, "rb")
    for line in fileObj: 
            count += line.count(keyword_bytes)
    fileObj.close()

    print(f"The word '{keyWordTtSearch}' appears {count} times in the {fileName} file.")




   

    # print(fileData.split(searchKeyWordInFile))

def main():
    if len(sys.argv) != 3:
       print("Please provide 2 as argument Filename and Keyword to search.")
       return
    
    fileName = sys.argv[1]
    keyWordTtSearch = sys.argv[2]

    searchKeyWordInFile(fileName, keyWordTtSearch) 

if __name__ == "__main__":
    main()