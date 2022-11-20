import things as tgs

def search_my_game(gameDat,kepemilikanDat,uid):

    _id = input('Masukkan ID Game: ')
    _releaseDate = input('Masukkan Tahun Rilis Game: ')

    result  = [[gameDat[0][0],gameDat[0][1],
                gameDat[0][4],gameDat[0][2],
                gameDat[0][3]]]

    filtered  = [[gameDat[0][0],gameDat[0][1],
                gameDat[0][4],gameDat[0][2],
                gameDat[0][3]]]

    for i in range(1,tgs.length(kepemilikanDat)):
        if (str(uid) in kepemilikanDat[i][1]):
            for j in range(1,tgs.length(gameDat)):
                if (gameDat[j][0] == kepemilikanDat[i][0]):
                    filtered += [[gameDat[j][0],gameDat[j][1],
                                gameDat[j][4],gameDat[j][2],
                                gameDat[j][3]]]
                
    for i in range(1,tgs.length(filtered)):
        #assign filter
        if (_id == ''):
            iD = filtered[i][0]
        else:
            iD = _id
        #assign filter
        if (_releaseDate == ''):
            rD = filtered[i][4]
        else:
            rD = _releaseDate
        #filter
        if (filtered[i][0] == iD and filtered[i][4] == rD) :
            result += [[filtered[i][0],filtered[i][1],
                        filtered[i][4],filtered[i][2],
                        filtered[i][3]]]
    print("Data game pada inventory yang memenuhi kriteria:")
    if(tgs.length(result)>1):
        tgs.print_game_data(result)
    else:
        print("Tidak ada game pada inventory-mu yang memenuhi kriteria")
