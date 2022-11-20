import things as tgs


def buy_game(user_id, gameDat, saldoDat, stokDat, riwayatDat):
    game_id = input("Masukkan ID game: ")

    indeks_game = -1
    indeks_stok = -1
    indeks_saldo = -1

    game_ada = False
    for i in range(1, tgs.length(gameDat)):
        if game_id == gameDat[i][0]:
            id_tidak_ada = False
            nama = gameDat[i][1]
            if user_id == gameDat[i][1]:
                game_ada = True
                indeks_game = i

    stok_tidak_ada = True
    id_tidak_ada = True
    for i in range(1, tgs.length(stokDat)):
        for j in range(0, 6):
            if game_id == stokDat[i][0]:
                nama = stokDat[i][1]
                id_tidak_ada = False
                indeks_stok = i
                if int(stokDat[indeks_stok][5]) > 0:
                    stok_tidak_ada = False

    if id_tidak_ada:
        return print("Tidak ada game dengan ID tersebut!")

    harga = float(stokDat[indeks_stok][4])

    saldo_tidak_ada = False
    for i in range(1, tgs.length(saldoDat)):
        for j in range(0, 6):
            if user_id == saldoDat[i][1]:
                indeks_saldo = i
                if float(saldoDat[indeks_saldo][5]) < harga:
                    saldo_tidak_ada = True

    if not game_ada and not saldo_tidak_ada and not stok_tidak_ada:
        stokDat[indeks_stok][5] = str(int(stokDat[indeks_stok][5]) - 1)
        saldoDat[indeks_saldo][5] = str(
            float(saldoDat[indeks_saldo][5]) - harga)
        print(f"Game {stokDat[indeks_stok][1]} berhasil dibeli")
        gameDat = tgs.tambahElemen(gameDat, [game_id, user_id])
        riwayatDat = tgs.tambahElemen(
            riwayatDat, [game_id, nama, harga, user_id, "2022"])
        return gameDat, stokDat, saldoDat, riwayatDat
    else:
        if game_ada:
            print("Anda sudah memiliki game tersebut!")
            return
        elif saldo_tidak_ada:
            print("Saldo anda tidak cukup untuk membeli game tersebut!")
            return
        elif stok_tidak_ada:
            print("Stok game tersebut sedang habis!")
