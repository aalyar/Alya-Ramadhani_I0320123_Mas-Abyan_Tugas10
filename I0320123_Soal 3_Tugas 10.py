print = ("Selamat datang di Program Biodata")
print = ("=================================")

# Mengambil output dari user
nama = input("Nama: ")
umur = input("Umur: ")
alamat = input("Alamat: ")

# format teks
teks = "Nama: {}\nUmur: {}\nAlamat: {}".format(nama, umur, alamat)

# buka file untuk ditulis

file_bio = open("biodata.txt", "a")

# menulis teks ke file
file_bio.write(teks)

#m menutup file
file_bio.close()
