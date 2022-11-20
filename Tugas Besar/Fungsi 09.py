import things as tgs


def list_game(user_id, gameDat, stokDat):
    game_list = [stokDat[0]]
    ambil_game_id = ['' for j in range(0, 1)]

    tidak_ada_game = True
    for i in range(1, tgs.length(gameDat)):
        for j in range(0, 1):
            if gameDat[i][1] == user_id:
                ambil_game_id[j] += gameDat[i][0] + ";"
                tidak_ada_game = False

    if tidak_ada_game:
        return print("Maaf, kamu belum membeli game. Ketik perintah buy_game untuk beli.")

    game_id_split = tgs.split(ambil_game_id[j], ";")

    for i in range(1, tgs.length(stokDat)):
        for j in range(tgs.length(game_id_split)):
            if game_id_split[j] == stokDat[i][0]:
                game_list += [stokDat[i]]

    print("Daftar game: ")
    tgs.print_game_data(game_list)
