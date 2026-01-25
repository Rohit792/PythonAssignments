"""
Question: Write a lambda function using filter () which accepts a list of numbers and returns a list of even numbers.

List of even number from [1, 2, 3, 4] is [2, 4]

"""

isEvenNumber = lambda number: (number % 2 == 0)

def main():
    listData = [1, 2, 3, 4]
    print(f" List of even number from {listData} is", list(filter(isEvenNumber, listData)))

if __name__ == "__main__":
    main()