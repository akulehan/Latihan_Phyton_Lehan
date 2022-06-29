#operator perbandingan, persamaan-pertidaksamaan
nama='sholehan'
pasw='Han814'
user=input('Masukkan nama user?')
#== operator sama dengan
#!= operator tidak sama dengan
if user == nama:
    print('User dikenali, lanjutkan...')
    input('Masukkan pasword Anda!')
    print('Anda berhasil masuk sistem.')
else:
    print('User tidak dikenal. Masukkan lagi.')