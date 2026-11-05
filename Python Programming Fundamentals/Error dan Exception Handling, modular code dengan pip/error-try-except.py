# exception akan terjadi saat program
# mengalami error saat runtime

# contoh sederhama utnuk menangkap exception
# input_user = int(input("masukkan angka: "))
# hasil = 0

# try:
#     hasil = 10/input_user
# except:
#     print("input tidak boleh 0")

# print(f"hasil = {hasil}")

# contoh di aplikasi
# while(True):
#     angka = int(input("masukkan angka pembagi: "))
#     try:
#         hasil = 10/angka
#         print(f"hasil = {hasil}")
#         is_done = input("lanjutkna (y/n)?")
#         if is_done == "n":
#             break
#     except:
#         print("pembagi 0, silahkan masukkan input lagi")

# print("Akhir dari program pembagi")

# contoh aplikasi untuk membuat file data.txt
while(True):
    try:
        with open("data.txt", "r") as file:
            print(file.read())
    except:
        print("file data.txt tidak ditemukan, membuat file baru")
        with open("data.txt", "w",encoding='utf=8') as file:
            file.write("file.baru")
        break

print("akhir dari program 2")