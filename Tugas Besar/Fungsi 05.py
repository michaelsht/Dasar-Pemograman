# Program Fungsi Mengubah Game pada Toko Game

import things as th


def ubah_Game (file) :
    # Mengubah game dengan mengisi informasi game yang akan diubah
    # Lalu, game akan disimpan dengan informasi baru dalam file csv
    # Admin tidak harus mengisi semua field selain field ID
    # Tidak bisa mengubah stock pada fungsional ini
    # Field ID tidak dapat diubah, hanya digunakan sebagai keyword pencari game
    # Validasi id yang di input ada pada file yang akan diubah
    valid = False
    id_Game = input("Masukkan ID game : ")
    for i in range(th.length(file)):
        if id_Game in file[i][0]:
            valid = True
            break

    if not valid:
        print ("Game tidak ditemukan")
    else:
        # Setelah melakukan validasi id dilanjutkan mengubah informasi
        Found = False
        for i in range (th.length(file)) :
            if file[i][0] == id_Game :
                nama_Game = input ("Masukkan nama game : ")
                if nama_Game != " " and th.isValidName(nama_Game) :
                    file[i][1] = nama_Game
                kategori = input ("Masukkan kategori : ")
                if kategori != " " and th.isValidKategori(kategori) :
                    file[i][2] = kategori
                tahun = input ("Masukkan tahun rilis : ")
                if tahun != " " and th.isValidTahun(tahun) :
                    file[i][3] = tahun
                harga = input ("Masukkan harga : ")
                if harga != " " and th.isValidHarga(harga) :
                    file[i][4] = harga
                Found = True
        if Found :
            print("Data berhasil diubah")
            return file