"""
Question: Write a lambda function using filter () which accepts a list of numbers and returns a list of numbers divisible by both 3 and 5.

Enter number of elements: 
5
Enter number 1: 21
Enter number 2: 11
Enter number 3: 15
Enter number 4: 12
Enter number 5: 1
List of elements are: 
 [21, 11, 15, 12, 1]

list of numbers divisible by both 3 and 5:
 [21, 15, 12]

"""

getStringGreaterThanFive = lambda number: (number % 5 == 0) or (number % 3 == 0)

def main():
    print("Enter number of elements: ")
    numberOfElements = int(input())
    listData = []
    for i in range(numberOfElements):
        listData.append(int(input(f"Enter number {i + 1}: ")))

    print(f"List of elements are: \n {listData}\n")
    print(f"list of numbers divisible by both 3 and 5:\n {list(filter(getStringGreaterThanFive, listData))}")

if __name__ == "__main__":
    main()