"""
Question: Write a program which accept one number form user and return addition of its factors.

Input : 12
Output : 16 (1+2+3+4+6)

"""

def getAdditionOfActors(number):
    factoorsAddition = 0
    listFactors = []

    for i in range(1, number):
        if number % i == 0:
            factoorsAddition = factoorsAddition + i
            listFactors.append(i)


    return (factoorsAddition, listFactors)
 
def main():
    number = int(input("Enter number: "))
    additionOfFactors = getAdditionOfActors(number)
    comma_separated_string = str(additionOfFactors[1])
    print(f"Addition of factors is {additionOfFactors[0]} {comma_separated_string}")

if __name__ == "__main__":
    main()