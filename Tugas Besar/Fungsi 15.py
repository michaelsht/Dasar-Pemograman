# made by Ammar 16521282
import argparse as ap
import os
import things as ts

user = []
game = []
riwayat = []
kepemilikan = []


def load():
    global user, game, riwayat, kepemilikan
    parser = ap.ArgumentParser()
    parser.add_argument("nama_folder", help="tulis nama folder yang sudah dibuat")
    args = parser.parse_args()

    directory = args.nama_folder
    path = os.getcwd() + "\\" + directory

    try:
        if os.path.isdir(path):
            print("Loading...")
            user = ts.read_csv(path + "\\user.csv")
            game = ts.read_csv(path + "\\game.csv")
            riwayat = ts.read_csv(path + "\\riwayat.csv")
            kepemilikan = ts.read_csv(path + "\\kepemilikan.csv")
            print("Selamat datang di antarmuka \"Binomo\" ")
        else:
            print(f'Folder "{directory}" tidak ditemukan.')
    except FileNotFoundError:
        print("Beberapa file tidak ditemukan di folder. Program tidak bisa lanjut.")
        exit(1)
