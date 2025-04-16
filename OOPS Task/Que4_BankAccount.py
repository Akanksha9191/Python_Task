# 4) Write a program which contains one class named as BankAccount.
# BankAccount class contains two instance variables as Name & Amount.
# That Class Contains one class variable as ROI which is initialize to 10.5
# Inside init method initialize all name and amount variable by accepting the values from user.
# There are four instance methods inside class as Display() , Deposit (), Withdraw( ), CalculateInterest()
# Deposit( ) method will accept the amount from user and add that value in class instance variable Amount.
# Withdraw() method will accept amount to be withdrawn from user and subtract that amount from class instance variable Amount.
# CalculateInterst() method calculate the interest based on Amount by considering rate of interest which is Class variable as ROI
# And Display () method will display value of all the instance variables as Name and Amount.
# After designing the above class call all instance methods by creating multiple objects


class BankAccount:
    
    ROI = 7.5
    
    def __init__(self):
        self.Name = ''
        self.Amount = 0.0
    
    def Accept(self):
        self.Name = input('Enter Account Holder Name : ')
        self.Amount = float(input('Enter Amount: '))
    
    def Deposite(self):
        self._Deposite = float(input('Enter Deposite Amount: '))
        self.Amount = self._Deposite + self.Amount
    
    def Withdraw(self):
        self._WithDraw = float(input("Enter Withdraw Amount: "))
        self.Amount =self.Amount + self._WithDraw
    
    def CalculateInterest(self):
        self._Interest = (self.Amount * BankAccount.ROI) / 100
              
    def Display(self):
        print('Account Holder Name: ', self.Name)
        print('Amount: ', self.Amount)
        print('-'*30)
        print('Deposite Amount:', self._Deposite)
        print('Withdraw Amount: ', self._WithDraw)
        print('Interest: ', self._Interest)
        
def main():
    bank = BankAccount()
    bank.Accept()
    bank.Deposite()
    bank.Withdraw()
    bank.CalculateInterest()
    bank.Display()

if __name__ == "__main__":
    main()