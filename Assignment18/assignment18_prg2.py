"""
Question: Write a program which accept N numbers from user and store it into List. Return addition of all elements from that List.

Input : 
Number of elements : 6
Input Elements : 13 5 45 7 4 56
Output : 56

"""
 
def getMaximumFrom(listData):
    maxNumber = listData[0]
    for i in range(1, len(listData)):
        if maxNumber < listData[i]:
            maxNumber = listData[i]

    return maxNumber

def main():
    number = int(input("Enter number of elements: "))
    listData = []

    for i in range(number):
        listData.append(int(input(f"Please enter elemnt at index {i}: ")))
    
    print("Maximum of element is: ", getMaximumFrom(listData))

if __name__ == "__main__":
    main()