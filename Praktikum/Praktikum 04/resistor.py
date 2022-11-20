def validate(r):
# Fungsi validasi input resistor
    return r > 0

def validatepil(pil):
# Fungsi validasi input pilihan
    return (pil == "s" or pil == "p")

def makeResistor(ar, pil):
# Fungsi pembuat resistor ekivalen
    if pil == 's':
        return ar[0] + ar[1] + ar[2]
    else:
        return (1/((1/r1) + (1/r2) + (1/r3)))

while True:
    r1 = float(input())
    r2 = float(input())
    r3 = float(input())
    pil = input().lower()
    if (validate(r1) and validate(r2) and validate(r3)):
        if validatepil(pil):
            print("%.2f" % (makeResistor([r1,r2,r3], pil)))
            break
        else:
            print("Masukan salah")
    else:
        print("Masukan salah")