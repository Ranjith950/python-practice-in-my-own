class BankAccount:
    def __init__(self,account_number,balance):
        self.account_num=account_number
        self.__balance=balance
    def deposit(self,amount):
        self.__balance += amount
    def display(self):
        print(f"Account_number: {self.account_num}")
        print(f"Balance: {self.__balance}")
account_number=int(input("Enter number:"))
balance=float(input("Enter balance:"))
deposit_amount=float(input("Enter amount"))
b=BankAccount(account_number,balance)

b.deposit(deposit_amount)
b.display()