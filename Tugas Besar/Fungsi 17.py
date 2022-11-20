import f15
import f16


def exit_program(username):
    save = ""
    if username is not None:
        while save.lower() != "y" and save.lower() != "n":
            save = input("Apakah Anda mau melakukan penyimpanan file? (y/n) ")

        if save.lower() == "y":
            f16.save(f15.user, f15.game, f15.riwayat, f15.kepemilikan)

    print("See you next time!")
    exit()
