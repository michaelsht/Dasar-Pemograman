# Nama          : Michael Sihotang
# NIM           : 16521201
# Spesifikasi   : Membaca masukan berat tubuh mahasiswa (dalam bentuk angka) dalam suatu kelas, sampai pengguna mengetikkan -999 (-999 tidak termasuk nilai yang diproses)
# Inisialisasi

x = int(input())
rata = berat50 = berat100 = siswa = 0
while (x!= -999) :
    if (x>=30 and x<=200) :
        siswa += 1
        if (x<=50) :
            berat50 += 1
        elif (x>=100) :
            berat100 += 1
        rata += x
    x = int(input())
if ( siswa == 0) :
    print("Data kosong")
else :
    print(siswa)
    print(berat50)
    print(berat100)
    print(round(rata/siswa))