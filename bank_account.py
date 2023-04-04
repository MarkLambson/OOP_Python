class BankAccount:
    def __init__(self, interestRate, balance):
        self.intrest_rate = interestRate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self
    
    def withdraw(self, amount):
        self.balance -= amount
        return self
    
    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self
    
    def yield_interest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.intrest_rate)
        else:
            print("Insufficient Funds")
        return self

bank_account1 = BankAccount(2.5, 250)
bank_account1.deposit(300).deposit(500).deposit(3000).withdraw(450).yield_interest().display_account_info()

bank_account2 = BankAccount(5, 20000)
bank_account2.deposit(50).deposit(250).withdraw(100).withdraw(100).withdraw(100).withdraw(1000).yield_interest().display_account_info()