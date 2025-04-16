# bank application using function:

def Bank(name, account_no, address, amount):
    print("-----Your Account Information----------")
    print(f'Account Holder Name: {name}')
    print(f'Account Number: {account_no}')
    print(f'Account Holder Address: {address}')
    print(f'Account Holder Amount: {amount}')
    
def main():
    Name = input('Enter Account holder name: ')
    AccountNumber = int(input('Enter Account Number: '))
    Address = input('Enter Account Holder Address: ')
    Amount = int(input('Enter Account Holder Amount: '))
    
    Bank(Name, AccountNumber, Address, Amount)

if __name__ == '__main__':
    main() 