"""
Question: Write a program which display first 10 even numbers on screen.
Output : 2 4 6 8 10 12 14 16 18 20 

"""

def displayFirstTenEvenNumbers():
    i = 1
    strValue = ""

    while len(strValue.split(" ")) <= 10:
        if i % 2 == 0:
            strValue = strValue + str(i) + " "
        i += 1
    print(strValue)

def main():
    displayFirstTenEvenNumbers()

if __name__ == "__main__":
    main()