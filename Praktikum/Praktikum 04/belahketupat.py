def GambarBelahKetupat(N):
    for i in range(1,N+1):
        if (i % 2 != 0):
            for j in range((N-i)//2):
                print(" ", end="")
            for j in range(i):
                print("*", end="")
            print()

    for i in range(N-1,0,-1):
        if (i % 2 != 0):
            for j in range((N-i)//2):
                print(" ", end="")
            for j in range(i):
                print("*", end="")
            print()


def IsValid(N):
    if (N % 2 == 1) and (N > 0) :
        return True
    else :
        return False

# ALGORITMA PROGRAM UTAMA
N = int(input())
if IsValid(N) == True:  # lengkapi dengan pemanggilan fungsi IsValid
    GambarBelahKetupat(N)    
else: 
    print("Masukan tidak valid")