import time


def magic_conch_shell():
    rng = (int(time.time()) & 0b1111) ^ 0b1010
    question = input('Tanyakan sesuatu pada Magic Conch Shell!\n')
    if (rng == 1 or rng == 2 or rng == 5):
        print("Ya")
    elif (rng == 3 or rng == 4 or rng == 13):
        print("Tidak")
    elif (rng == 6 or rng == 0 or rng == 14):
        print("Bisa Jadi")
    elif (rng == 7 or rng == 8 or rng == 11):
        print("Tentunya")
    else:
        print("Tidak mungkin")
