from BankAccount import BankAccount


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.accounts = []
    
    def add_account(self, account):
        self.accounts.append(account)
    
    def make_deposit(self, account_idx, amount):
        if 0 <= account_idx < len(self.accounts):
            self.accounts[account_idx].deposit(amount)
        else:
            print("Invalid account index.")
    
    def make_withdrawal(self, account_idx, amount):
        if 0 <= account_idx < len(self.accounts):
            self.accounts[account_idx].withdraw(amount)
        else:
            print("Invalid account index.")
    
    def display_user_balance(self, account_idx):
        if 0 <= account_idx < len(self.accounts):
            print(f"User: {self.name}, Account Balance: {self.accounts[account_idx].balance}")
        else:
            print("Invalid account index.")
    
    def transfer_money(self, amount, other_user, from_account_idx, to_account_idx):
        if 0 <= from_account_idx < len(self.accounts) and 0 <= to_account_idx < len(other_user.accounts):
            if self.accounts[from_account_idx].balance >= amount:
                self.accounts[from_account_idx].withdraw(amount)
                other_user.accounts[to_account_idx].deposit(amount)
                print("Transfer successful.")
            else:
                print("Insufficient funds for transfer.")
        else:
            print("Invalid account index.")

# Example usage:
user1 = User("Mounir", "mounir@gmail.com")
user2 = User("Said", "said@gmail.com")

user1_account = BankAccount(int_rate=0.02, balance=100)
user2_account = BankAccount(int_rate=0.02, balance=200)

user1.add_account(user1_account)
user2.add_account(user2_account)

user1.make_deposit(0, 50)
user1.display_user_balance(0)

user1.make_withdrawal(0, 30)
user1.display_user_balance(0)

user1.transfer_money(20, user2, 0, 0)
user1.display_user_balance(0)
user2.display_user_balance(0)
