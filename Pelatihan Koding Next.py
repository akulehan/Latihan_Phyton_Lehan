#-----------enter
print("Selamat pagi semuanya... :)")
print("Nama saya Sholehan \n")
# \n" digunakan untuk 1 baris enter
print("Saya mengikuti pelatihan coding bersama Kominfo dan Koding Next")
print("Sesi hari ini adalah coding menggunakan python. Dengan python kita dapat membuat program-program.")

#-----------input dan output
print ("\n")
print("Halo anak-anak!")
#print ("\n") digunakan untuk double baris enter,
print("Bapak akan meminta kalian mengetik warna lampu lalu lintas")
#input untuk meminta user menginputkan 
warna = input("Ketikkan warna lampu lalu lintas di sini : ")

#-----------conditional statement
#if else jika kondisinya hanya satu
#if elif jika kondisinya lebih dari satu
#ingat harus ada tanda titik dua
if warna == "merah":
    print("Bagus. Warna merah berarti berhenti")
elif warna == "kuning":
    print("Bagus. Warna kuning berarti hati-hati")
elif warna == "hijau":
    print("Bagus. Warna hijau berarti jalan terus")
else:
    print("Maaf. Tidak ada warna itu di lampu lalu lintas... :)")
