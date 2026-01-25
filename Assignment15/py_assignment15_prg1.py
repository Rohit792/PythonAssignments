"""
Question: Write a lambda function using map () which accepts a list of numbers and returns a list of squares of each number.

Square of [10, 20, 30, 40] is [100, 400, 900, 1600]

"""

getSquareOf = lambda number: number ** 2

def main():
    listData = [10, 20, 30, 40]
    print(f"Square of {listData} is ", list(map(getSquareOf, listData)))

if __name__ == "__main__":
    main()