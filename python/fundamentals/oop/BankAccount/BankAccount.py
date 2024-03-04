class BankAccount:
    def __init__(self, int_rate=0.01, balance=0):
        self.interest_rate = int_rate
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        return self
    
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        return self
    
    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self
    
    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.interest_rate
        return self

    @classmethod
    def print_all_accounts_info(cls, accounts):
        for account in accounts:
            account.display_account_info()

# Create two accounts
account1 = BankAccount().deposit(100).deposit(50).deposit(200).withdraw(75).yield_interest().display_account_info()
account2 = BankAccount().deposit(200).deposit(100).withdraw(50).withdraw(100).withdraw(25).withdraw(75).yield_interest().display_account_info()

# Print all instances of a Bank Account's info using classmethod
BankAccount.print_all_accounts_info([account1, account2])
