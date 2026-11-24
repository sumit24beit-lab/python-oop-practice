class BankAccount:
    def __init__(self, account_number, customer_name, balance):
        self.account_number=account_number
        self.customer_name=customer_name
        self.balance=balance
    def deposit(self, amount):
        if amount > 0:
            self.balance = self.balance + amount
            print(f"Deposited Amount: ₹{amount}")
        else: 
            print("Invalid Deposit Amount!")
    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid Withdrawal Amount!")
        elif amount > self.balance:
            print("Transaction Failed: Insufficient Balance!")
        else:
            self.balance = self.balance - amount
            print(f"Withdrawal Amount: ₹{amount}")
    def display_balance(self):
        print(f"Current Account Balance: ₹{self.balance}")
    def display_details(self):
        print(f"Account Number: {self.account_number}")
        print(f"Customer Name: {self.customer_name}")
        print(f"Account Balance: ₹{self.balance}\n")
account1=BankAccount(1001, "Amit", 10000)
account2=BankAccount(1002, "Priya", 8000)
print("========== BANK ACCOUNT MANAGEMENT ==========\n")
account1.display_details()
account1.deposit(5000)
account1.withdraw(3000)
account1.display_balance()
print("\n---------------------------------------------\n")
account2.display_details()
account2.deposit(2000)
account2.withdraw(12000)
account2.display_balance()


    