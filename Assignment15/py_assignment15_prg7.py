"""
Question: Write a lambda function using filter () which accepts a list of strings and returns a list of strings having length greater than 5.

List of String is:
 ['Jay', 'Ganesh', 'list', 'of', 'Machine', 'Python']

Length greater than 5:
 ['Ganesh', 'Machine', 'Python']

"""

getStringGreaterThanFive = lambda stringElement: len(stringElement) > 5
def main():
    listData = ["Jay", "Ganesh", "list", "of", "Machine", "Python"]
    print(f"List of String is:\n {listData}\n")
    print(f"Length greater than 5:\n {list(filter(getStringGreaterThanFive, listData))}")

if __name__ == "__main__":
    main()