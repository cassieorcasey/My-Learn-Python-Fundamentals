# Operator Aritmatika
a = 10
b = 3

print(a + b) # Penjumlahan
print(a - b) # Pengurangan
print(a * b) # Perkalian
print(a / b) # Pembagian

print(a // b) # Pembagian Bulat
print(a % b) # Modulo

# Contoh Modulo
print(10 % 2)
print(11 % 2)

a = 2
b = 3

print(a ** b) # Pangkat

# Contoh lain
print(5 ** 2) # 5 Pangkat 2
print(3 ** 4) # 3 Pangkat 4

x = 10
print("x awal:", x)

x += 5 # Sama dengan: x = x + 5
print("x setelah += 5:", x) # 15

x -= 3 # Sama dengan: x = x - 3
print("x setelah -= 3:", x) # 12

x *= 2 # Sama dengan: x = x * 2
print("x setelah *= 2:", x) # 24

x /= 4 # Sama dengan: x = x / 4
print("x setelah /= 4:", x) # 6.0

# Operator Pembandingan
print(a > b) # Lebih besar: True
print(a < b) # Lebih kecil: False
print(a >= b) # Lebih besar atau sama: True
print(a <= b) # Lebih kecil atau sama: False
print(a == b) # Sama dengan: False
print(a != b) # Tidak sama dengan: True

nama1 = "Cassandra"
nama2 = "Cassie"
nama3 = "Cassandra"

print(nama1 == nama3) # True
print(nama2 == nama1) # False
print(nama1 != nama2) # True

# Operator Logika
umur = 16
print(umur > 15 and umur < 30) # (16 > 15 dan 16 < 30) True

hari = "Rabu"
print(hari == "Sabtu" or hari == "Minggu") # False

aktif = True
print(not aktif) # False

# Operator String
nama_depan = "Cassandra"
nama_belakang = "Cassie"
nama_lengkap = nama_depan + " " + nama_belakang
print(nama_lengkap) # Cassandra Cassie

kata = "Hello"
print(kata * 3) #HelloHelloHello

garis = "-"
print(garis * 10) # ----------

kalimat = "Cassandra dari San Fransisco"
print("San Francisco" in kalimat) # True
print("Cassie" in kalimat) # False
print("Cassandra" in kalimat) # True