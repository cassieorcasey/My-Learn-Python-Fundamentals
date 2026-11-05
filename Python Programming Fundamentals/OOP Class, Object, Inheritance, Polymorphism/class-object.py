# Contoh class
# class Mahasiswa:
#     pass

# class Jurusan:
#     pass

# Contoh class dengan object
# jurusan1 = Jurusan()
# jurusan2 = Jurusan()

# print(type(jurusan1))
# print(type(jurusan2))

# mahasiswa1 = Mahasiswa()
# mahasiswa2 = Mahasiswa()

# print(type(mahasiswa1))
# print(type(mahasiswa2))

# instance attributes

# mahasiswa1 = Mahasiswa()
# mahasiswa1.nim = "222"
# mahasiswa1.nama = "Karina"

# print(mahasiswa1.nim)
# print(mahasiswa1.nama)

# mahasiswa2 = Mahasiswa()
# mahasiswa2.nim = "456"
# mahasiswa2.nama = "Cassandra"

# print(mahasiswa2.nim)
# print(mahasiswa2.nama)

# Class Attributes

# class Jurusan:
#     nama_jurusan = ""
#     alamat = ""

# jurusan = Jurusan()
# print(jurusan.nama_jurusan)
# print(jurusan.alamat)

# class Mahasiswa:
#     nim = 0
#     nama = ""

# mahasiswa = Mahasiswa()
# print(mahasiswa.nim)
# print(mahasiswa.nama)

# Class dengan Methods

# class Mahasiswa:
#     nim = 0
#     nama = ""

#     def perkenalana(self):
#         print(f"Perkenalkan, nama saya {self.nama}")

# mahasiswa = Mahasiswa()
# mahasiswa.nama = "Karina"
# mahasiswa.perkenalana()

# Paramaters dengan Methods

# class Mahasiswa:
#     nim = 0
#     nama = ""

#     def perkenalan(self):
#         print(f"Perkenalkan, nama saya {self.nama} dan nim saya {self.nim}")

#     def hello(self, nama):
#         print(f"Halo {nama}, nama saya {self.nama}")

# mahasiswa = Mahasiswa()
# mahasiswa.nama = "Karina"
# mahasiswa.nim = "222"
# mahasiswa.perkenalan()
# mahasiswa.hello("Cassandra")