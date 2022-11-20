import os
import things as ts


def save(user=None, game=None, riwayat=None, kepemilikan=None):
    folder = input("Masukkan nama folder penyimpanan: ")
    abs_path = os.getcwd() + "\\" + folder
    print("Saving...")

    if not os.path.exists(abs_path):
        os.makedirs(abs_path)

    if user is not None:
        ts.write_csv(abs_path + "\\user.csv", user)
    if game is not None:
        ts.write_csv(abs_path + "\\game.csv", game)
    if riwayat is not None:
        ts.write_csv(abs_path + "\\riwayat.csv", riwayat)
    if kepemilikan is not None:
        ts.write_csv(abs_path + "\\kepemilikan.csv", kepemilikan)

    print("Data telah disimpan di " + folder + "!")
