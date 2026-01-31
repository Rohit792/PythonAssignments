"""
Question: Write a program which display 5 times Marvellous on screen.

Output :
Marvellous Marvellous Marvellous Marvellous Marvellous

"""

def main():
    strValue = ""
    for _ in range(5):
        strValue = strValue + "Marvellous "
    print(strValue)

if __name__ == "__main__":
    main()