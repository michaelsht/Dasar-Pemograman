N = int(input())

while N <= 0 or N > 100:
    print('Masukan salah. Ulangi!') 
    N = int(input())

m = [int(input()) for i in range(N)] 
x = int(input())

done = False 

if x == 0:
    for i in range(N):
        if m[i] == 0 and not done:
            print(i+1)
            done = True
    if not done: print('Tidak ada 0')
elif x == -1:
    for i in range(N):
        if m[i] < 0 and not done:
            print(i+1, m[i])
            done = True
    if not done: print('Tidak ada negatif')
elif x == 1:
    for i in range(N):
        if m[i] > 0 and not done:
            print(i+1, m[i])
            done = True
    if not done: print('Tidak ada positif')
else: print('Tidak diproses')