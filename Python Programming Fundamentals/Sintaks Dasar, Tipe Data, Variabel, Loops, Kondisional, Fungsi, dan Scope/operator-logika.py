# Kondisi dengan Operator Logika
umur = int(input("Masukkan Umur Anda: "))
punya_ktp = input("Punya KTP? (ya/tidak): ")

if umur >= 17 and punya_ktp == "ya":
    print("Punya KTP")
else:
    print("Tidak Punya KTP/Masih Dibawah Umur")