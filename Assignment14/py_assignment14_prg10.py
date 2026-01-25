"""
Question: Write a lambda function which accepts three numbers and returns largest number.

Enter Number1: 21
Enter Number2: 101
Enter Number3: 11
Largest Number is: 101

"""
getGreaterFrom = lambda number1, number2: number1 if number1 > number2 else number2
getLargestOf = lambda number1, number2, number3: getGreaterFrom(getGreaterFrom(number1, number2), number3)

def main():
    number1 = int(input("Enter Number1: "))
    number2 = int(input("Enter Number2: "))
    number3 = int(input("Enter Number3: "))

    print("Largest Number is: ", getLargestOf(number1, number2, number3))

if __name__ == "__main__":
    main()



