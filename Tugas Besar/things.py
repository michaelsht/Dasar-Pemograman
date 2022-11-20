import os


def read_csv(filename, delimiter=';'):
    with open(filename) as file:
        parse = []
        for line in file:
            values = split(line, delimiter)
            parse += [values]
    return parse


def write_csv(filename, to_write):
    with open(filename, "w") as file:
        rows = length(to_write)
        if rows != 0:
            cols = length(to_write[0])  # karena jumlah column sama tiap garis
            for i in range(rows):
                for j in range(cols):
                    file.write(str(to_write[i][j]))
                    if j < cols-1:
                        file.write(";")
                if i < rows-1:
                    file.write("\n")
        else:
            print("Matriks kosong! Tidak bisa menuliskan file.")


def split(string, split_str):
    delimiter = '"\t\n'
    delimiter += split_str

    output = []
    word = ''
    for i in string:
        if i not in delimiter:
            word += i
        elif word:
            output += [word]
            word = ''
    if word:
        output += [word]
    return output


def length(array):
    i = 0
    for _ in array:
        i += 1
    return i


def print_game_data(gameDat, offset=0):
    spacing = [2 for i in range(0, length(gameDat[0]))]
    for i in range(1-offset, length(gameDat)-offset):
        for j in range(0, length(gameDat[0])):
            if (spacing[j] < (length(gameDat[i][j]) + 2)):
                spacing[j] = length(gameDat[i][j]) + 2

    content = ['' for i in range(0, length(gameDat[0]))]

    for i in range(1-offset, length(gameDat)-offset):
        for j in range(0, length(gameDat[0])):
            content[j] = gameDat[i][j]

        output = ''
        for j in range(0, length(gameDat[0])):
            if (j != length(gameDat[0])-1):
                output += ("{1:<{0}s}| ".format(spacing[j], content[j]))
            else:
                output += ("{1:<{0}s}".format(spacing[j], content[j]))

        print(str(i+offset)+". "+output)


def cariElemen(i, array):
    # Mencari elemen dalam array
    # KAMUS
    # found = bool
    # ALGORITMA
    found = False
    for a in range(length(array)):
        if array[a] == i:
            found = True
    return found


def tambahElemen(array, a):
    # Menambahkan elemen pada array di belakang
    # KAMUS
    # X : array pengganti
    # i : int
    # ALGORITMA
    X = [0 for i in range(length(array) + 1)]
    for i in range(length(array) + 1):
        if i != length(array):
            X[i] = array[i]
        else:
            X[i] = a
    return X


def isGameInFile(cek, namaGame):
    for i in range(length(namaGame)):
        if cek == namaGame[i][1]:
            return True
    return False


def isValidName(nama):
    # Fungsi untuk melakukan validasi nama
    # type nama adalah string
    nama = str(nama)
    lengthNama = length(nama)
    if lengthNama > 0:
        # Nama tidak boleh kosong
        for i in range(lengthNama):
            if nama[i] not in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890-_ ":
                return False
    return True


def isValidKategori(kategori):
    kategori = str(kategori)
    lengthKategori = length(kategori)
    if lengthKategori > 0:
        for i in range(lengthKategori):
            if kategori[i] not in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz-_ ":
                return False
    return True


def isValidTahun(tahun):
    tahun = str(tahun)
    lengthTahun = length(tahun)
    if lengthTahun > 0:
        for i in range(lengthTahun):
            if tahun[i] not in "1234567890":
                return False
    else:
        return False

    # Tahun valid ada direntang tahun 1920 - 2022
    if 1920 <= int(tahun) <= 2022:
        return True
    else:
        return False


def isValidHarga(harga):
    harga = str(harga)
    lengthHarga = length(str(harga))
    string = ""
    # Syarat harga hanya ada angka 0-9 dan tanda titik
    for i in range(lengthHarga):
        if harga[i] in "1234567890.":
            string = string + harga[i]
    if int(string) > 0:
        return True
    return False


def isValidStok(stok):
    stok = str(stok)
    lengthStok = length(str(stok))
    if lengthStok > 0:
        for i in range(lengthStok):
            if stok[i] not in "1234567890":
                return False
    return True


def cariUsername(i, file):
    # Mencari elemen dalam array
    # KAMUS
    # found = bool
    # ALGORITMA
    found = False
    for a in range(length(file)):
        if file[a][1] == i:
            found = True
    return found


def minimum(i, j):
    return i if i < j else j


def __minimum_run(n):
    r = 0
    while n >= 32:
        r |= n & 1
        n >>= 1
    return n + r


def __insertion_sort(array, left, right):
    for i in range(left + 1, right + 1):
        elmt = array[i]
        j = i - 1
        while elmt < array[j] and j >= left:
            array[j+1] = array[j]
            j -= 1
        array[j+1] = elmt
    return array


def __merge(array, l, m, r):
    l1 = m - l + 1
    l2 = r - m
    left = []
    right = []
    for i in range(0, l1):
        left += [array[l + i]]
    for i in range(0, l2):
        right += [array[m + i + 1]]

    i, j, k = 0, 0, l

    while i < l1 and j < l2:
        if left[i] <= right[j]:
            array[k] = left[i]
            i += 1
        else:
            array[k] = right[j]
            j += 1
        k += 1

    while i < l1:
        array[k] = left[i]
        k += 1
        i += 1

    while j < l2:
        array[k] = right[j]
        k += 1
        j += 1


def timsort(array):
    l = length(array)
    min_run = __minimum_run(l)

    for start in range(1, l, min_run):
        end = minimum(start + min_run - 1, l - 1)
        __insertion_sort(array, start, end)
    size = min_run
    while size < l:
        for left in range(1, l, 2*size):
            mid = minimum(l - 1, left + size - 1)
            right = minimum(left + 2*size - 1, l - 1)
            __merge(array, left, mid, right)
        size = 2 * size
    return array
