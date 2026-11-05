class BankAccount:
    __no = ""
    __balance = 0

    def __init__(self,no):
        self.__no = no

    def get_balance(self):
        return self.__balance

    def topup(self, amount):
        self.__balance += amount

    def cashout(self, amount):
        if amount > self.__balance:
            raise ValueError("Saldo tidak mencukupi")
        self.__balance -= amount

cassandra_account = BankAccount("cassandra")
cassandra_account.topup(100000)
print(cassandra_account.get_balance())
cassandra_account.cashout(50000)
print(cassandra_account.get_balance())