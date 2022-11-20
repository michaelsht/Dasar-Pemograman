N = int(input())
C1 = input()
C2 = input()

if N <= 0 :
    print('Masukan tidak valid')
elif C1 == C2 :
    print('Masukan tidak valid')
else :
    for i in range (N) :
        for j in range (N-1) :
            if i == 0 or i == N-1 :
                print(C1, end='')
            else :
                if j != 0 and j != N-1 :
                    print(C2, end='')
                else :
                    print(C1, end='')
        print(C1)