import things as tgs


def list_game_toko(stokDat):
    skema = input("Skema sorting: ")
    if skema == "":
        tgs.print_game_data(tgs.timsort(stokDat))
    else:
        for i in range(1, tgs.length(stokDat)-1):
            for j in range(i+1, tgs.length(stokDat)-1):
                if skema == "tahun+":
                    if (int(stokDat[i][3]) > int(stokDat[j][3])):
                        stokDat[i], stokDat[j] = stokDat[j], stokDat[i]
                elif skema == "tahun-":
                    if (int(stokDat[i][3]) < int(stokDat[j][3])):
                        stokDat[i], stokDat[j] = stokDat[j], stokDat[i]
                elif skema == "harga+":
                    if (int(stokDat[i][4]) > int(stokDat[j][4])):
                        stokDat[i], stokDat[j] = stokDat[j], stokDat[i]
                elif skema == "harga-":
                    if (int(stokDat[i][4]) < int(stokDat[j][4])):
                        stokDat[i], stokDat[j] = stokDat[j], stokDat[i]
                else:
                    return print("Skema sorting tidak valid")

        tgs.print_game_data(stokDat)
