"""
Question: Write a program which accept N numbers from user and store it into List. Accept one another number from user and return frequency of that number from List.

Input : 
Number of elements : 11
Input Elements : 13 5 45 7 4 56 5 34 2 5 65
Element to search : 5
Output : 3


"""
 
def getSearchCountFrom(listData, elementToSearch):
    searchCount = 0

    for i in range(1, len(listData)):
        if elementToSearch == listData[i]:
            searchCount += 1

    return searchCount

def main():
    number = int(input("Enter number of elements: "))
    listData = []

    for i in range(number):
        listData.append(int(input(f"Please enter elemnt at index {i}: ")))
    
    elementToSearch = int(input("Enter element to search: "))

    print("Search count of element is: ", getSearchCountFrom(listData, elementToSearch))

if __name__ == "__main__":
    main()