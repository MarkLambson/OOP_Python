class BankAccount:
    def __init__(self, interestRate, balance):
        self.intrest_rate = interestRate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self
    
    def withdraw(self, amount):
        if self.balance > amount:
            self.balance -= amount
        else:
            print("Insufficient Funds: Charging a $5 fee")
            self.balance -= 5
        return self
    
    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self
    
    def yield_interest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.intrest_rate)
        else:
            print("error: negative balance")
        return self

class User:
    def __init__(self, firstName, lastName):
        self.first_name = firstName
        self.last_name = lastName
        self.account = BankAccount(interestRate=.5, balance=1000)
    def make_deposit(self, amount):
        self.account.deposit(amount)
        print(self.account.balance)
        return self
    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
        print(self.account.balance)
        return self
    def display_user_balance(self):
        print(f"{self.first_name} {self.last_name} has a balance of: ${self.account.balance}")
        return self



user1 = User("John", "Doe")
user1.display_user_balance().make_deposit(9000).display_user_balance()