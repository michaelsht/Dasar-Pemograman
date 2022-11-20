# Nama      : Michael Sihotang
# NIM       : 16521201
def bubbleSort(arr,n):
    for i in range(n-1):
        for j in range(0, n-i-1):
 
           
            if arr[j] > arr[j + 1] :
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

N = int(input())
arr = [0 for i in range(N)]

for i in range (N):
    arr[i] = int(input())
bubbleSort(arr,N)

X = int(input())

if X == arr[0] or X == arr[N-1]:
    if X == arr[N-1]:
        print("maksimum")
    if X == arr[0]:
        print("minimum")
else:
    valid = False
    for i in range(1,N-1):
        if X == arr[i]:
            valid = True
    if valid:
        print("N#A")
    else:
        X = str(X)
        print(X + " tidak ada")