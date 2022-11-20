import things as tgs


def search_game_at_store(gameDat):

    filter = ['' for i in range(0,5)]
    
    filter[0] = input('Masukkan ID Game: ')
    filter[1] = input('Masukkan Nama Game: ')
    filter[4] = input('Masukkan Harga Game: ')
    filter[2] = input('Masukkan Kategori Game: ')
    filter[3] = input('Masukkan Tahun Rilis Game: ')

    result  = [gameDat[0]]
    filter2 = ['' for i in range(0,5)]
    for i in range(1,tgs.length(gameDat)):
        for j in range(0,5):
            if (filter[j] == ''):
                filter2[j] = gameDat[i][j]
            else:
                filter2[j] = filter[j]
        
        filter3 = 0
        for j in range(0,5):
            if (gameDat[i][j] == filter2[j]):
                filter3 = filter3 + 1
        #filter
        if (filter3 == 5) :
            result += [gameDat[i]]

    print("Data game pada toko yang memenuhi kriteria:")
    if(tgs.length(result)>1):
        tgs.print_game_data(result)
    else:
        print("Tidak ada game pada toko yang memenuhi kriteria")
