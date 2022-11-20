# Program Fungsi Login

import things as th
import B1

def login(file) :
    # Saat masuk ke dalam aplikasi, pengguna bisa login dengan memasukkan username dan password. 
    # Bila cocok dengan file user maka berhasil login
    # KAMUS
        # username, password : str
        # i, id, : int
        # found : bool
    # ALGORITMA
    username = input('Masukkan username: ')
    password = input('Masukkan password: ')
    
    # inisialisasi nilai a = 0 agar saat pengondisian menemukan nilai a = 0 berarti username atau password salah
    a = 0
    # Pengecekan data username dan password pada file
    for i in range (th.length(file)) :
        if file [i][1] == username and B1.decrypt(file [i][3]) == password :
            a = 1
            break

    # Pengondisian nilai dari id yang telah ada di inisialisasi
    if a == 0 : 
        print (f'Password atau username salah atau tidak ditemukan.')
        return None
    else : 
        nama = file [i][2]
        print (f'Halo {nama} ! Selamat datang di "Binomo".')
        return username