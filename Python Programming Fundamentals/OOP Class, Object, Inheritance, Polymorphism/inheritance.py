# class Parent
# class Kendaraan:
#     def __init__(self, merk, tahun):
#         self.merk = merk
#         self.tahun = tahun

#     def info(self):
#         return f"Merk: {self.merk}, Tahun: {self.tahun}"

#     def nyalakan(self):
#         print(f"{self.info()} dinyalakan")

# class Child Mobil:
# class Mobil(Kendaraan):

#     def klakson(self):
#         print(f"Mobil {self.info()} memiliki klakson")

# avanza = Mobil("Avanza", 2019)
# avanza.nyalakan()
# avanza.klakson()

# class Child Motor
# class Motor(Kendaraan):

#     def klakson(self):
#         print(f"Motor {self.info()} memiliki klakson")

# scoopy = Motor("Scoopy", 2018)
# scoopy.nyalakan()
# scoopy.klakson()

# Function Super() - Akses Parent Class
# class Child Mobil
# class Mobil(Kendaraan):
#     def __init__(self, merk, tahun, jumlah_roda):
#         super().__init__(merk, tahun)
#         self.jumlah_roda = jumlah_roda

#     def klakson(self):
#         print(f"Mobil {self.info()} memiliki klakson")

# avanza = Mobil("Avanza", 2019, 4)
# avanza.nyalakan
# avanza.klakson
# print(avanza.jumlah_roda)

# Method Overriding
# class Child Motor
# class Motor(Kendaraan):

#     def klakson(self):
#         print(f"Motor {self.info()} tidak memilki klakson")

#     def nyalakan(self):
#         # jika ingin menggunakan method nyalakan dari parent class
#         # super().nyalakan()
#         print(f"Motor {self.merk} dinyalakan secara otomatis")

# scoopy = Motor("Scoopy", 2018)
# scoopy.nyalakan()
# scoopy.klakson()

# Multilevel Inheritance
class Karyawan:
    def __init__(self, nama, gaji):
        self.nama = nama
        self.gaji = gaji

class KaryawanTetap(Karyawan):
    pass

class Manager(KaryawanTetap):
    pass

class VicePresident(Manager):
    pass

# Multiple Inheritance
# class BisaBerenang:
#     def berenang(self):
#         print("Bisa Berenang")

# class BisaBerlari:
#     def berlari(self):
#         print("Bisa Berlari")

# class Atlit(BisaBerenang, BisaBerlari):
#     def __init__(self, nama):
#         self.nama = nama

# cassandra = Atlit("Cassandra")
# cassandra.berenang()
# cassandra.berlari()

# Diamond Problem
# class A:
#     def method(self):
#         return "Method from A"

# class B:
#     def method(self):
#         return "Method from B"

# class C(A):
#     def method(self):
#         return "Method from C"

# class D(B, C):
#     pass

# Python menggunakan Methodo Resolution Order (MRO)
# d = D()
# print(d.method())

# Type Checking
cassandra = Karyawan("Cassandra", 1000000)
karina = KaryawanTetap("Karina", 1000000)
cassie = Manager("Cassie", 1000000)
cassey = VicePresident("Cassey", 1000000)

print(isinstance(cassandra, Karyawan))
print(isinstance(karina, Karyawan))
print(isinstance(cassie, Karyawan))
print(isinstance(cassey, Karyawan))