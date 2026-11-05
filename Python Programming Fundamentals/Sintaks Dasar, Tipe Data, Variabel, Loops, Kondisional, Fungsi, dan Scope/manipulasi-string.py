nama = "Cassandra"
umur = 16

# Cara yang salah (akan error)
# pesan = "Nama saya " + nama + " dan umur saya " + umur + " tahun"

# Cara yang benar
pesan = "Nama saya " + nama + " dan umur saya " + str(umur) + " tahun"
print(pesan) # menampilkan nilai variabel pesan

print(len(nama)) # menampilkan panjang string variabel nama
print(len(pesan)) # menampilkan panjang string variabel pesan

nama = "Cassandra"
print(nama[0]) # menampilkan karakter pertama dari string variabel nama
print(nama[1]) # menampilkan karakter kedua dari string variabel nama
print(nama[2]) # menampilkan karakter ketiga dari string variabel nama
print(nama[3]) # menampilkan karakter keempat dari string variabel nama

print(nama[-1]) # menampilkan karakter terakhir dari string variabel nama
print(nama[-2]) # menampilkan karakter kedua dari belakang dari string variabel nama
print(nama[-3]) # menampilkan karakter ketiga dari belakang dari string variabel nama

nama = "Cassandra"
print(nama[0:3])
print(nama[2:5])
print(nama[3:5])

nama = "Cassandra"
print(nama)
nama_upper = nama.upper()
print(nama_upper)
nama_lower = nama.lower()


nama = "cassie"
nama_title = nama.title()
print(nama_title)
nama_captalized = nama.capitalize

nama = "    Cassandra    "
nama_strip = nama.strip()
print(nama_strip)

kalimat = "aku anak dari steve jobs"
kalimat_baru = kalimat.replace("steve jobs", "jensen huang")
print(kalimat_baru)

nama = "cassanda huang"
jumlah_a = nama.count("a")
print(jumlah_a)

kalimat = "i love windows"
posisi = kalimat.find("windows")
print(posisi)

kalimat = "Baris pertama\nBaris kedua"
print(kalimat)

kalimat = "Nama:\tCassandra\nUmur:\t16"
print(kalimat)

lokasi = "C:\\Users\Cassandra\Dekstop"
print(lokasi)

kalimat = "he say \"hello\" to me"
print(kalimat)

nama = "Cassandra"
umur = "16"
kota = "San Francisco"

# Menggunakan f-string
portofolio = f"Halo, nama saya {nama}, umur saya {umur} tahun, asal kota saya di {kota}"
print(portofolio)

# Better dibandingkan concatenation
portofolio_smk = "Halo, nama saya " + nama + ", umur " + str(umur) + " tahun, tinggal di " + kota
print(portofolio_smk)

harga = 100000
jumlah = 3

# Operasi matematika dalam f-string
total = f"total: Rp {harga * jumlah}"
print(total)

nama = "cassandra"
kalimat = f"Hello {nama.upper()}"
print(kalimat)