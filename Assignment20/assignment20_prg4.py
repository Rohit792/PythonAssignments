"""
Question:
Design a Python application that creates three threads named Small, Capital, and Digits.
• All threads should accept a string as input.
• The Small thread should count and display the number of lowercase characters.
• The Capital thread should count and display the number of uppercase characters.
• The Digits thread should count and display the number of numeric digits.
• Each thread must also display:
    • Thread ID
    • Thread Name

Name:  101 Jay Ganesh
Thread id: 6173683712
Thread Name:  Thread-1 (Small)
Total number of lowercase:  7

Thread id: 6190510080
Thread Name:  Thread-2 (Capital)
Total number of Uppercase:  2

Thread id: 6173683712
Thread Name:  Thread-3 (Digits)
Total number of Digits   :  3

"""
import threading
 
def Small(strValue):
    print(f"Thread id: {threading.get_ident()}")
    print(f"Thread Name: ",threading.current_thread().name)

    countLowerCaseChar = 0
    for i in range(len(strValue)):
        if ord(strValue[i]) >= 97 and ord(strValue[i]) <= 122:
         countLowerCaseChar += 1
    print("Total number of lowercase: ", countLowerCaseChar)

def Capital(strValue):
    print(f"Thread id: {threading.get_ident()}")
    print(f"Thread Name: ",threading.current_thread().name)
    
    countUpperCaseChar = 0
    for i in range(len(strValue)):
        if ord(strValue[i]) >= 65 and ord(strValue[i]) <= 90:
         countUpperCaseChar += 1
    print("Total number of Uppercase: ", countUpperCaseChar)

def Digits(strValue):
    print(f"Thread id: {threading.get_ident()}")
    print(f"Thread Name: ",threading.current_thread().name)

    countDigits = 0
    for i in range(len(strValue)):
        if ord(strValue[i]) >= 48 and ord(strValue[i]) <= 57:
         countDigits += 1
    print("Total number of Digits   : ", countDigits)

def main():
   strValue = "101 Jay Ganesh"
   print("Name: ", strValue)
   smallThread = threading.Thread(target= Small, args=(strValue,))
   smallThread.start()

   capitalThread = threading.Thread(target= Capital, args=(strValue,))
   capitalThread.start()

   digitsThread = threading.Thread(target= Digits, args=(strValue,))
   digitsThread.start()
   
if __name__ == "__main__":
    main()