# Creating class
class BankAccount:
    def __init__(self, account_number, account_holder , balance):
        self.account = account_number
        self.name = account_holder
        self.current_balance = balance
        
# Method to deposit amount
    def deposit(self,amount):
        self.current_balance += amount
        print("deposit sucessful")

# Method to withdraw
    def withdraw(self,amount):
        if self.current_balance >= amount:
            self.current_balance -= amount
            print("Withdrawl successful")
        else:
            print("Balance low")
    
# Method to print balance
    def get_balance(self):
        print(f"current balance = {self.current_balance}")

# Creating a object and printing 
acc1 = BankAccount("Saswat",23445,55000.00)
acc1.deposit(5000)
acc1.withdraw(2000)
acc1.get_balance()
