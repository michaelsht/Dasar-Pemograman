import things as tgs

def topup(userDat):
    ind = -1
    user = input("Masukkan username: ")
    add = float(input("Masukkan saldo: "))
    for i in range(1,tgs.length(userDat)):
        if(userDat[i][1] == user):
            ind = i
    if(ind < 0):
        print("Username \"{0}\" tidak ditemukan.".format(user))
        return userDat
    if(add<0):
        print("Masukan tidak valid.")
        return userDat

    userDat[ind][5] = str(float(userDat[ind][5]) + add)

    print("Top up berhasil. Saldo {0}" 
            " bertambah menjadi {1}".format(userDat[ind][2],userDat[ind][5]))
    return userDat
