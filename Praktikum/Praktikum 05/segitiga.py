# Nama          : Michael Sihotang
# NIM           : 16521201
# Spesifikasi   : Menghitung luas segitiga
# Input
a=input()
# Inisialisasi
b=0
# Proses
for i in a:
    if i == " ":
        b=a.index(i)
        break

alas=int(a[0:b])
tinggi=int(a[b+1:])

if not(alas >0 and tinggi>0):
    print('Alas dan tinggi harus > 0')
else:
    luas=round(alas*tinggi/2)
    print(luas)