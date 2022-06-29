#-----------evaluation sistem

#---input
print("Halo, selamat datang di penilaian sistem evaluasi")
print("Program ini akan membantu para guru untuk cek nilai para siswa")
print("Tolong masukkan nilainya, akan saya hitung.")
print("\n")
nama = input("Nama Siswa :")
kelas = input("Kelas :")
nis = input("Nomor Induk Siswa :")
mapel = input("Mata Pelajaran :")
nilai1 = input("Masukkan nilai pertama :")
nilai2 = input("Masukkan nilai kedua :")
total = int(nilai1) + int(nilai2)
rerata = (int(nilai1) + int(nilai2))/2
#int adalah konverter dari string ke integer
print("\n")

#---concatenation (dengan tanda plus (+))
#str adalah konverter dari integer ke string
print("Nama Siswa :" + nama)
print("Kelas :" + kelas)
print("Nomor Induk Siswa :" + nis)
print("Mata Pelajaran :" + mapel)
print("Masukkan nilai pertama :" + nilai1)
print("Masukkan nilai kedua :" + nilai2)
print("Nilai total kamu :" + nilai1 + "+" + nilai2 + " = " + str(total))
print("Nilai rata-rata kamu :" + "(" + nilai1 + "+" + nilai2 + ")/2 = " + str(rerata) + "\n")

#conditional statement
if rerata >= 90:
    print("Nilaimu A. Usaha yang bagus!")
elif rerata >=80:
    print ("Nilaimu B. Hebat. Semoga nilaimu lebih bagus.")
elif rerata >=70:
    print ("Nilaimu C. Belajar lagi ya... Yakin nilaimu pasti lebih bagus.")
else:
    print ("Nilaimu D. Ayo belajar lebih giat lagi!")
