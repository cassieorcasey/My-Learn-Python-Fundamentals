# Decorator

# class Matematika:

#    @staticmethod
#    def tambah(a, b):
#         return a + b

# result = Matematika.tambah(22, 2)
# print(result)

# Class Method

# class BankAccount:
#     no = ""
#     balance = 0
#     active = True

#     def  __init__(self, no, balance=0):
#         self.no = no
#         self.balance = balance

#     @classmethod
#     def disabled(cls, no, balance=0):
#         account = cls(no, balance)
#         account.active = False
#         return account

# bank_account1 = BankAccount("1", 1000)
# bank_account2 = BankAccount.disabled("2", 2000)
# print(f"Bank account {bank_account1.no} has balance {bank_account1.balance} and status {bank_account1.active}")
# print(f"Bank account {bank_account2.no} has balance {bank_account2.balance} and status {bank_account2.active}")

# Property Metthods untuk Mengontorol Akses

# class Category:
#     _name = ""

#     def set_name(self,name):
#         if name == "":
#             raise ValueError("Nama kategori tidak boleh kosong")
#         self._name = name

#     def get_name(self):
#         return self._name

# category1 = Category()
# category1.set_name("Apple")
# print(category1.get_name())

# Property Decorator

class Category:
    _name = ""

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if name == "":
            raise ValueError("Nama tidak boleh kosong")
        self._name = name

category1 = Category()
category1.name = "Nvidia"
print(category1.name)