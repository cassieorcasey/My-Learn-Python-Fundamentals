point = (5, 10)
print(point[0]) # 5
print(point[1]) # 10

# Untuk data yang tidak berubah
tanggal_lahir = (29, 10, 2010) # tanggal, bulan, tahun lahir
print("Tanggal lahir:", tanggal_lahir)

# iterasi di tuple
for e in tanggal_lahir:
    print(e)

# iterasi di tuple dengan index
for i in range(len(tanggal_lahir)):
    print(tanggal_lahir[i])