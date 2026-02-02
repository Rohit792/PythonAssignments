"""
Question:
1:  Write a Python program to implement a class named BankAccount with the following requirements:
• The class should contain two instance variables:
    • Name (Account holder name)
    • Amount (Account balance)

• The class should contain one class variable:
    • ROI (Rate of Interest), initialized to 10.5
• Define a constructor (__init__) that accepts Name and initial Amount.
• Implement the following instance methods:
    • Display () - displays account holder name and current balance
    • Deposit () - accepts an amount from the user and adds it to balance
    • Withdraw() - accepts an amount from the user and subtracts it from balance (Ensure withdrawal is allowed only if sufficient balance exists)
    • CalculateInterest () - calculates and returns interest using formula:
Interest = (Amount * ROI) / 100
• Create multiple objects and demonstrate all

output:
Current balance of Rohit is 1000
Please enter amount to diposit: 500
Please enter amount to Withdraw: 300
Interest on amount is:  126.0
Current balance of Rohit is 1200.0
---------------------------
Current balance of Mangesh is 200
Please enter amount to diposit: 300
Please enter amount to Withdraw: 50
Interest on amount is:  47.25
Current balance of Mangesh is 450.0
"""

class BankAccount:
    ROI = 10.5

    def __init__(self, Name, Amount):
        self.Name = Name
        self.Amount = Amount
 
    def Display(self):
        print(f"Current balance of {self.Name} is {self.Amount}")

    def Deposit(self):
        self.Amount = self.Amount + float(input("Please enter amount to diposit: "))

    def Withdraw(self):
        withdrawAmount = float(input("Please enter amount to Withdraw: "))
        if withdrawAmount > self.Amount:
            print(f"Amount must be less than current balence({self.Amount})")
        else:
            self.Amount = self.Amount - withdrawAmount
    
    def CalculateInterest(self):
       print("Interest on amount is: ", (self.Amount * self.ROI) / 100)

 
if __name__ == "__main__":
    Objl = BankAccount("Rohit", 1000)
    Objl.Display()
    Objl.Deposit()
    Objl.Withdraw()
    Objl.CalculateInterest()
    Objl.Display()
    print("---------------------------")
    Obj2 = BankAccount("Mangesh", 200)
    Obj2.Display()
    Obj2.Deposit()
    Obj2.Withdraw()
    Obj2.CalculateInterest()
    Obj2.Display()
 

     
