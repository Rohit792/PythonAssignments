"""
Question: Write a program which accept N numbers from user and store it into List. Return Minimum number from that List.

Input : 
Number of elements : 4
Input Elements : 13 5 45 7
Output : 5


"""
 
def getMinimumFrom(listData):
    miniNumber = listData[0]
    for i in range(1, len(listData)):
        if miniNumber > listData[i]:
            miniNumber = listData[i]

    return miniNumber

def main():
    number = int(input("Enter number of elements: "))
    listData = []

    for i in range(number):
        listData.append(int(input(f"Please enter elemnt at index {i}: ")))
    
    print("Minimum number is: ", getMinimumFrom(listData))

if __name__ == "__main__":
    main()