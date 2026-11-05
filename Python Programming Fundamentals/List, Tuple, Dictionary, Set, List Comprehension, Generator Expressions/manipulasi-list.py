# mengakses elemen
buah = ["apel", "jeruk", "pisang", "mangga"]
print(buah[0]) # apel
print(buah[1]) # jeruk
print(buah[2]) # pisang
print(buah[-1]) # mangga (elemen terakhir)

# mengubah elemen
warna = ["merah", "biru", "hijau"]
print(warna)
warna[1] = "kuning"
print(warna) # ["merah", "kuning", "hijau"]

# menambah elemen
buah = ["apel", "jeruk"]
print(buah)
buah.append("pisang")
print(buah)
buah.insert(1, "alpukat")
print(buah)

buah.remove("jeruk")
print(buah)

buah.pop()
print(buah)

del buah[0]
print(buah)

buah = ["apel", "pisang", "jeruk"]
print(len(buah))

satu = [1,2,3,4,5]
print(satu)
dua = [6,7,8,9,10]
print(dua)

gabungan = satu + dua
print(gabungan)

beberapa_buah = ["apel", "pisang", "alpukat", "pepaya"]
for buah in beberapa_buah:
    print(buah)

for i in range(0, len(beberapa_buah)):
    print(beberapa_buah[i])

if "apel" in beberapa_buah:
    print("ada apel")
else:
    print("Tidak ada apel")