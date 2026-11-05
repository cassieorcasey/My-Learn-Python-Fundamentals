# class BankAccount:
#     def __init__(self, no, balance=0):
#         self.no = no
#         self.balance = balance

#     def transfer(self, amount):
#         if amount > self.balance:
#             raise ValueError("Saldo tidak mencukupi")
#         self.balance -= amount

# try:
#     bank_account = BankAccount("123456", 100)
#     bank_account.transfer(1000000)
# except ValueError as e:
#     print(f"Errror: {e}")

# Custom Exceptions Class
class BalanceNotEnough(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message

class BankAccount:
    def __init__(self, no, balance=0):
        self.no = no
        self.balance = balance

    def transfer(self, amount):
        if amount > self.balance:
            raise BalanceNotEnough("Saldo tidak mencukupi")
        self.balance -= amount

try:
    bank_account = BankAccount("123456", 100)
    bank_account.transfer(1000000)
except BalanceNotEnough as e:
    print(f"Error {e}") 
    