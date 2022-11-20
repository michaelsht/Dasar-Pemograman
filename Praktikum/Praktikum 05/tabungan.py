# Nama          : Michael Sihotang
# NIM           : 16521201
# Spesifikasi   : Membaca masukan jumlah tabungan dari sejumlah siswa

# Input
N = int(input())
# Inisialisasi
s = 0
# Proses
for i in range(N):
    x = int(input())
    s = s + x
# Output
print(s)