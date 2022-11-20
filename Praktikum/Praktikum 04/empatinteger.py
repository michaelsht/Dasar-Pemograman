def CekInteger (x):
    if x == 0:
        print("NOL")
    elif x > 0:
        print("POSITIF")
    else:
        print("NEGATIF")
              
def Max (a, b, c, d):
    ar = [a,b,c,d]
    max = a
    for i in range(4):
        if ar[i] > max:
            max = ar[i]
    return max
            
def Min (a, b, c, d):
    ar = [a,b,c,d]
    min = a
    for i in range(4):
        if ar[i] < min:
            min = ar[i]
    return min

def IsAllPositif (a, b, c, d):
    ar = [a,b,c,d]
    for i in range(4):
        if ar[i] <= 0:
            return False
    return True
            
# PROGRAM UTAMA
# Tidak boleh diubah-ubah
# Input
A = int(input())
B = int(input())
C = int(input())
D = int(input())

# Menuliskan sifat integer
CekInteger(A)
CekInteger(B)
CekInteger(C)
CekInteger(D)

# Penulisan maksimum, minimum, dan mean olympic
if (IsAllPositif(A,B,C,D)):
    print(Max(A,B,C,D))
    print(Min(A,B,C,D))
    mo = (A + B + C + D - Max(A,B,C,D) - Min(A,B,C,D)) / 2
    print("%.2f" % mo)