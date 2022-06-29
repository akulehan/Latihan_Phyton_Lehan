print("Selamat datang...")
nama = input ("Silahkan masukkan nama?")
#concenation bisa pakai tanda plus (+) atau koma (,)
print("Halo,", nama)
nilai = input ("Masukkan nilaimu?")
#input angka berupa string, jadi harus diubah menjadi integer
nilaiint = int(nilai)
if nilaiint > 90:
    print("Nilaimu", nilai , "maka predikat A")
elif nilaiint > 80:
    print("Nilaimu", nilai , "maka predikat B")
elif nilaiint > 70:
    print("Nilaimu", nilai , "maka predikat C")
else:
    print("Nilaimu", nilai , "maka predikat D")