# Dictionary dengan data
siswa = {
    "nama": "Cassandra",
    "kelas": 10,
    "jurusan": "RPL",
}
print(siswa)

print(siswa["nama"])
print(siswa["kelas"])
print(siswa["jurusan"])

# Mengubah nilai
siswa["kelas"] = 11
print(siswa)

# Menghapus key-value
del siswa["jurusan"]
print(siswa)

# Mengiterasi keys
for key in siswa:
    print(key, ":", siswa[key])

# Mengiterasi key-value pairs
for key, value in siswa.items():
    print(key, ":", value)
