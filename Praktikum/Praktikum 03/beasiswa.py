# Nama    : Michael Sihotang
# NIM     : 16521201
# Tanggal : 03 Maret 2022

ip = float(input())
pdpt = float(input())

if ip >= 3.5 :
  print(4)
elif 1 <= pdpt < 5 and ip < 3.5 :
  if ip >= 2 :
    print(3)
  else :
    print(2)
elif pdpt < 1 and ip < 3.5 :
  print(1)
else :
  print(0)