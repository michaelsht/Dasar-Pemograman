import things as tgs


def ubah_stok(gameDat):
    game_id = input("Masukkan ID Game: ")

    indeks_game = -1
    ada_game = False
    stok_awal = 0
    for i in range(1, tgs.length(gameDat)):
        for j in range(0, 5):
            if game_id == gameDat[i][0]:
                ada_game = True
                indeks_game = i
                stok_awal = int(gameDat[i][5])

    if ada_game:
        stok = int(input("Masukkan perubahan jumlah stok: "))
    else:
        print("Tidak ada game dengan ID tersebut!")
        return gameDat

    temp = stok + int(gameDat[indeks_game][5])
    if temp >= 0:
        gameDat[indeks_game][5] = temp

    if temp < 0:
        print(
            f"Stok game {gameDat[indeks_game][1]} gagal dikurangi karena stok kurang. Stok sekarang: {stok_awal} (< {abs(stok)}) ")
    else:
        if gameDat[indeks_game][5] < stok_awal:
            print(
                f"Stok game {gameDat[indeks_game][1]} berhasil dikurangi. Stok sekarang: {gameDat[indeks_game][5]}")
        else:
            print(
                f"Stok game {gameDat[indeks_game][1]} berhasil ditambahkan. Stok sekarang: {gameDat[indeks_game][5]}")
    gameDat[indeks_game][5] = str(gameDat[indeks_game][5])
    return gameDat
