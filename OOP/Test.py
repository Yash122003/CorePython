class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private variable

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance  # Balance ko access karne ka method


# Usage
account = BankAccount(1000)
account.deposit(500)
print(account.get_balance())  # Output: 1500
