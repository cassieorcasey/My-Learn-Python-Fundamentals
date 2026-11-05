# Pernyataan if
angka = int(input("Masukkan Angka: "))

if angka > 0:
    print("Angka Positif")

if angka < 0:
    print("Angka Negatif")

if angka == 0:
    print("Angka nol")

# Pernyataan if-else
nilai = int(input("Masukkan Angka:"))

if nilai >= 80:
    print("Lulus")
else:
    print("Tidak Lulus")

# Pernyataan else-if (elif)
nilai = int(input("Masukkan nilai: "))

if nilai >= 90:
    print("A")
elif nilai >= 80:
    print("B")
elif nilai >= 70:
    print("C")
elif nilai >= 60:
    print("D")
else:
    print("E")

# nested if (if bersarang)
username = input("Masukkan Username: ")
password = input("Massukkan Password: ")

if username == "admin":
    if password == "123456":
        print("Login berhasil")
        print("Selamat Datang Admin")
    else:
        print("password salah")
else:
    print("Username tidak ditemukan")

# Pernyataan Match Case
hari = input("?Masukkan nama hari: ").lower()

match hari:
    case "senin" | "selasa" | "rabu" | "kamis" | "jumat":
        print("Hari Produktif")
    case "sabtu" | "minggu":
        print("Hari Santai")
    case _:
        print("Nama hari tidak valid")

# Conditional Expression
angka = int(input("Masukkan angka: "))

# Contoh dengan if-else biasa
if angka > 0:
    hasil = "Positif"
else:
    hasil = "Non-positif"

# Contoh dengan ternary operator
hasil = "Positif" if angka > 0 else "Non-positif"
print("Angka tersebut: ", hasil)