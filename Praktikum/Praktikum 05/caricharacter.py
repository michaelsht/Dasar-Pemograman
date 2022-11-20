# Nama      : Michael Sihotang
# NIM       : 16521201
while True:
    N = int(input())
    if 0 < N <= 100:
        break
    else:
        print("Masukan salah. Ulangi!")

arr = [0 for _ in range(N)]

for i in range(N):
    arr[i] = input()

CC = input().lower()

state = False

if CC == "s":
    for y in range(N):
        if 97 <= ord(arr[y]) <= 122:
            state = True
            no = y
            stake = arr[y]
            break
    if state:
        print(no+1,stake)
    else:
        print("Tidak ada huruf kecil")
elif CC == "l":
    for i in range(N):
        if 65 <= ord(arr[i]) <= 90:
            state = True
            no = i
            stake = arr[i]
            break
    if state:
        print(no+1,stake)
    else:
        print("Tidak ada huruf besar")
elif CC == "x":
    for i in range(N):
        if not((65 <= ord(arr[i]) <= 90) or (97 <= ord(arr[i]) <= 122)):
            state = True
            no = i
            stake = arr[i]
            break
    if state:
        print(no+1,stake)
    else:
        print("Semua huruf")
else:
    print("Tidak diproses")

