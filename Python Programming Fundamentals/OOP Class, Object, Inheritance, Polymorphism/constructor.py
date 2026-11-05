# Tanpa Constructor

class Mahasiswa:
    nim = 0
    nama = ""

    def __init__(self, nim, nama): # Manual setup
        self.nim = nim
        self.nama = nama

# Harus panggil setup manual
mhs = Mahasiswa(222, "Karina")

print(mhs.nim)
print(mhs.nama)

# Constructor dengan Validation

# class BankAccount:
#     no = ""
#     saldo = 0

#     def __init__(self, no, saldo=0):
        # validasi saldo
        # if saldo < 0:
        #     raise ValueError("Saldo tidak boleh negatif")

# karina = BankAccount("123456789", 1000) # sukses
# cassandra = BankAccount("987654321", -500) # error

# Method String

class Mahasiswa:
    nim = 0
    nama = ""

    def __init__(self, nim, nama): # Manual setup
        self.nim = nim
        self.nama = nama

    def __str__(self):
        return f"Mahasiswa(nim={self.nim}, nama={self.nama})"

# Harus panggil setup manual
mhs = Mahasiswa(222, "Karina")
print(f"Info {mhs}")

# Methods untuk Object Comparison

def __eq__(self, other):
    return self.nim == other.nim and self.nama == other.nama

mhs = Mahasiswa(222, "Karina")
mhs = Mahasiswa(222, "Karina")
print(mhs == mhs) # True