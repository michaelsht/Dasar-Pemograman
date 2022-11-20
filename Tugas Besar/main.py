import F2
import F3
import F4
import F5
import f06
import f07
import f08
import f09
import f10
import f11
import f12
import f13
import f14
import f15
import f16
import f17
import things as ts


def main_menu(username):
    # Pengecekan jika admin atau user biasa
    role = ""
    for i in range(ts.length(f15.user)):
        if username == f15.user[i][1]:
            role = f15.user[i][4]
            break
    print("Selamat datang di main menu program BNMO!")

    while True:
        print()
        command = input("Masukkan perintah: ")

        # Admin only commands
        if command.lower() == "register":  # F2
            if role == "admin":
                f15.user = F2.register(f15.user)
            else:
                print("Perintah ini hanya bisa diakses oleh admin.")
        elif command.lower() == "add_game":  # F4
            if role == "admin":
                f15.game = F4.tambah_Game(f15.game)
            else:
                print("Perintah ini hanya bisa diakses oleh admin.")
        elif command.lower() == "change_game_info":  # F5
            if role == "admin":
                f15.game = F5.ubah_Game(f15.game)
            else:
                print("Perintah ini hanya bisa diakses oleh admin.")
        elif command.lower() == "change_game_stock":  # F6
            if role == "admin":
                f15.game = f06.ubah_stok(f15.game)
            else:
                print("Perintah ini hanya bisa diakses oleh admin.")
        elif command.lower() == "top_up":  # F12
            if role == "admin":
                f15.user = f12.topup(f15.user)
            else:
                print("Perintah ini hanya bisa diakses oleh admin.")
        # User only commands
        elif command.lower() == "buy_game":  # F8
            if role == "user":
                temp = f08.buy_game(username, f15.kepemilikan, f15.user, f15.game, f15.riwayat)
                if temp is not None:
                    f15.kepemilikan, f15.game, f15.user, f15.riwayat = temp
            else:
                print("Perintah ini hanya bisa diakses oleh user.")
        elif command.lower() == "list_owned":  # F9
            if role == "user":
                f09.list_game(username, f15.kepemilikan, f15.game)
            else:
                print("Perintah ini hanya bisa diakses oleh user.")
        elif command.lower() == "search_owned":  # F10
            if role == "user":
                f10.search_my_game(f15.game, f15.kepemilikan, username)
            else:
                print("Perintah ini hanya bisa diakses oleh user.")
        elif command.lower() == "search_store":  # F11
            if role == "user":
                f11.search_game_at_store(f15.game)
            else:
                print("Perintah ini hanya bisa diakses oleh user.")
        elif command.lower() == "history":  # F13
            if role == "user":
                f13.riwayat(username, f15.riwayat)
            else:
                print("Perintah ini hanya bisa diakses oleh user.")
        # Role-agnostic commands
        elif command.lower() == "list_games":
            f07.list_game_toko(f15.game)
        elif command.lower() == "help":  # F14
            f14.help(username, f15.user)
        elif command.lower() == "save":  # F16
            f16.save(f15.user, f15.game, f15.riwayat, f15.kepemilikan)
        elif command.lower() == "exit":
            f17.exit_program(username)
        else:
            print("Perintah tidak dikenal. Ketik \"help\" untuk list semua perintah yang dikenal.")


if __name__ == "__main__":
    f15.load()
    print()
    print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
    print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
    print("&&&&&&&&&&        &&&#    &&&&  &&&     &&&&&     &&&&         &&&&&&&&&&&&")
    print("&&&&&&&&&&   &&&   &&#     &&&  &&&  ,   &&&      &&.  %&&&&&   &&&&&&&&&&&")
    print("&&&&&&&&&&        #&&#  &/  ,&  &&&  ,&  .&.  &   &&   &&&&&&   &&&&&&&&&&&")
    print("&&&&&&&&&&   &&&&  .&#  &&&     &&&  ,&&  .  &&   &&   &&&&&&   &&&&&&&&&&&")
    print("&&&&&&&&&&         &&#  &&&&    &&&  ,&&%   &&&   &&&*        .&&&&&&&&&&&&")
    print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
    print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
    print()
    while True:
        cmd = input("Masukkan perintah: ")
        username = None
        if cmd.lower() == "login": # F3
            username = F3.login(f15.user)
            if username is not None:
                main_menu(username)
                break
        elif cmd.lower() == "help":  # F14
            f14.help(username, f15.user)
        elif cmd.lower() == "exit":  # F17
            f17.exit_program(None)
        else:
            print("Perintah tidak dikenal. Ketik \"help\" untuk list semua perintah yang dikenal.")
        print()
