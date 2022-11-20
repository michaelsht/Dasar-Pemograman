import things as ts


def help(username, user):
    # Searching
    idx = 0
    for i in range(ts.length(user)):
        if username == user[i][1]:
            idx = i
            break

    print("============ HELP ============")
    if username is not None:
        if user[idx][4] == "admin":
            print("register          - Untuk melakukan registrasi user baru")
            print("add_game          - Menambah suatu game ke list game")
            print("change_game_stock - Mengubah stok game")
            print("change_game_info  - Mengubah info pada game")
            print("top_up            - Menambah/mengurang saldo")
        else:
            print("buy_game          - Membeli game")
            print("list_owned        - List game yang dimiliki")
            print("search_owned      - Mencari game yang dimiliki")
            print("search_store      - Mencari game di toko")
            print("history           - Menunjukkan riwayat pembelian user")
        print("list_games        - Mencetak semua game di toko")
        print("help              - Menunjukkan list perintah")
        print("save              - Menyimpan segala perubahan")
        print("exit              - Keluar dari program")
    else:
        print("login             - Login ke sistem")
        print("help              - Menunjukkan list perintah")
        print("exit              - Keluar dari program")