# Game tebak angka dengan break
angka_rahasia = 7

while True:
    tebakan = int(input("Tebak angka (1-10): "))

    if tebakan == angka_rahasia:
        print("Selamat! Anda benar!")
        break
    else:
        print("Salah, coba lagi!")