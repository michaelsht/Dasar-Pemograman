# Program Fungsi Register

import things as th
import B1

def register(file) :
    # Program dapat mendaftarkan pengguna baru dengan memasukkan nama, username, dan password.
    # Username harus unik (tidak bisa ada username yang sama)
        # KAMUS
        # nama, username, password, passwordValid : str
    # ALGORITMA
    nama = input ('Masukkan nama : ')
    username = input ('Masukkan username : ') 
    password = input ('Masukkan password : ')
    encrypted = B1.encrypt(password)

    # Pengondisian agar username unik
    if th.cariUsername (username, file) :
        print (f'Username {username} sudah terpakai, silakan menggunakan username lain.')
    else :
        print (f'Username {username} telah berhasil register ke dalam "Binomo".')
        return th.tambahElemen (file, [(th.length(file) + 1), username, nama, encrypted, "user", "0"])
