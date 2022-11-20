# Program Fungsi Menambah Game ke Toko Game

import things as th


def tambah_Game (file) :
    # Penambahan game dilakukan melalui pengisian informasi game yang akan ditambahkan.
    # Program melakukan validasi mengenai semua informasi yang dibutuhkan
    # Pengguna akan diminta input informasi sampai tervalidasi oleh program
    namaGame = input ("Masukkan nama game: ")
    kategori = input ("Masukkan kategori game: ")
    tahun = input ("Masukkan tahun rilis game: ")
    harga = input ("Masukkan harga game: ")
    stok = input ("Masukkan stok awal: ") 

    # Melakukan validasi mengenai semua informasi yang dibutuhkan
    valid = False
    while not valid: 
        # Cek apakah game yang ditambahkan sudah ada pada file
        if th.isGameInFile(namaGame, file) :
            print("Game sudah ada pada toko, silakan menammbahkan game lain")
            namaGame = input("Masukkan nama game: ")
            kategori = input("Masukkan kategori game: ")
            tahun = input("Masukkan tahun rilis game: ")
            harga = input("Masukkan harga game: ")
            stok = input("Masukkan stok awal: ") 
        # Setelah cek game selesai dilanjutkan cek informasi yang dibutuhkan
        else:
            # Validasi semua informasi 
            if th.isValidName(namaGame) and th.isValidKategori(kategori) and th.isValidTahun(tahun) and th.isValidHarga(harga) and th.isValidStok(stok) :
                valid = True 
            # Ketika ada informasi yang tidak tervalidasi
            else:
                print("Mohon masukkan semua informasi mengenai game agar dapat disimpan BNMO")
                namaGame = input("Masukkan nama game: ")
                kategori = input("Masukkan kategori game: ")
                tahun = input("Masukkan tahun rilis game: ")
                harga = input("Masukkan harga game: ")
                stok = input("Masukkan stok awal: ")
    print (f"Selamat! Berhasil menambahkan game {namaGame}.") 
    return th.tambahElemen (file, ["GAME" + '%03d' % (th.length(file) + 1), namaGame, kategori, tahun, harga, stok])