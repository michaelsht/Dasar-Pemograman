import things as tgs

def riwayat(userID,riwayatDat):
    result = [[riwayatDat[0][0],riwayatDat[0][1],str(riwayatDat[0][2]),riwayatDat[0][4]]]
    
    for i in range(1,tgs.length(riwayatDat)):
        if(riwayatDat[i][3]==userID):
            result += [[riwayatDat[i][0],riwayatDat[i][1],str(riwayatDat[i][2]),riwayatDat[i][4]]]

    if(tgs.length(result)==1):
        print("Maaf, kamu tidak ada riwayat pembelian game."
                " Ketik perintah 'buy_game' untuk membeli.")
    else:
        print("Daftar game:")
        tgs.print_game_data(result)



