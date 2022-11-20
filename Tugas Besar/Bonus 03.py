# TUGAS BESAR DASAR PEMOGRAMAN
# BONUS 03 - Game Tic-Tac-Toe
# Kelompok 10

import things as th
# Program Game Tic-Tac-Toe
# Program ini akan menjalankan sebuah game Tic-Tac-Toe dengan ada 2 pemain yaitu X dan O

# Kamus
# papan : array of int
# count : int
# manang, inGame, seri : Bool

# Algoritma
# Inisialisasi
papan = ['#', '#', '#', '#', '#', '#', '#', '#', '#']
count = 0                   # untuk melacak tempat yang sudah berisi
menang = False              # untuk mengecek apakah ada yg menang atau tidak
inGame = True               # untuk mengecek apakah game harus dilanjutkan atau tidak
seri = False                # untuk mengecek apakah game terjadi seri atau tidak 
pemainSekarang = 'X'        
detail = [] 

# Fungsi untuk mengetahui urutan pemain Game Tic-Tac-Toe
def urutan(pemainSekarang): 
    # Kamus lokal 
    # pemainSekarang : string

    # Algoritma 
    # Untuk melakukan pengurutan bahwa pemain X dan O akan bermain secara bergantian     
    if pemainSekarang == 'X':
        return ['O', 'X']
    else :
        return ['X', 'O']

# Fungsi untuk menampilkan papan bermain
def statusPapan(papan):
    # Algoritma
    print('Status Papan')
    print( papan[0] +' | ' + papan[1] +' | ' + papan[2])
    print( papan[3] +' | ' + papan[4] +' | ' + papan[5])
    print( papan[6] +' | ' + papan[7] +' | ' + papan[8])

# Fungsi ini mengecek pemenang secara diagonal, horizontal, dan vertikal
def cekMenang(marker, pemain):
    # Kamus Lokal
    # marker : str (variabel untuk X atau O)

    # Algoritma
    if ((papan[0] == marker and papan[1] == marker and papan[2] == marker) or 
        (papan[3] == marker and papan[4] == marker and papan[5] == marker) or
        (papan[6] == marker and papan[7] == marker and papan[8] == marker) or
        (papan[0] == marker and papan[3] == marker and papan[6] == marker) or
        (papan[1] == marker and papan[4] == marker and papan[7] == marker) or
        (papan[1] == marker and papan[5] == marker and papan[8] == marker) or
        (papan[3] == marker and papan[5] == marker and papan[7] == marker)):
        print('Pemain', pemain, 'menang.')
        return True
    else :
        return False 

# Fungsi untuk cek apakah input berada di tempat yang kosong
def insert_input(jumlahIsi, marker):
    while papan[jumlahIsi] != '#':
        print("Kotak sudah terisi, silakan untuk mengisi kotak yang lain")
        jumlahIsi = int(input())
    papan[jumlahIsi] = marker 

# PROGRAM UTAMA
print(">>> tictactoe")
print("""Legenda:
    # Kosong 
    X Pemain 1
    O Pemain 2""")
while inGame:
    statusPapan(papan)
    print(f'Giliran Pemain "{pemainSekarang}"')
    A = int(input("X : "))
    B = int(input("Y : "))
    # Pengondisian untuk letak dari input X dan O
    if A == 1 and B == 1:
        input_slot = 1
    elif A == 2 and B == 1:
        input_slot = 2
    elif A == 3 and B == 1:
        input_slot = 3
    elif A == 1 and B == 2:
        input_slot = 4
    elif A == 2 and B == 2:
        input_slot = 5
    elif A == 3 and B == 2:
        input_slot = 6
    elif A == 1 and B == 3:
        input_slot = 7
    elif A == 2 and B == 3:
        input_slot = 8
    elif A == 3 and B == 3:
        input_slot = 9
    else :
        print("Kotak tidak valid.")

    # Mengurutkan pemain agar bermain secara bergantian
    detail = urutan(pemainSekarang)
    pemainSekarang = detail[0]

    # Mengecek input
    insert_input(input_slot-1, detail[1])
    count = count + 1

    # Menentukan pemenang
    menang = cekMenang(detail[1], detail[1])
    if count == 9 and not menang:
        print("Permainan seri / Tidak ada pemenang")
        seri = True
        statusPapan(papan)
    
    # Pengondisian untuk bertanya apakah akan bermain lagi atau tidak
    if menang or seri:
        mainLagi = input("Apakah kamu ingin bermain lagi? Silakan mengetik Y/y untuk yes atau N/n untuk no : ")
        if mainLagi == 'Y' or mainLagi == 'y':
            for j in range(0, th.length(papan)):
                papan[j] = '#'
        elif mainLagi == "N" or "n" :
            print("Terima kasih sudah bermain, selamat melanjutkan aktivitas!")
            inGame = False
inGame