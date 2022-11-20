import things as ts


# Vigenere Cipher
def encrypt(password):
    password = password.lower()
    cipher = []
    start = ord('a')
    key = "tubesdaspro"
    i = 0
    for j in range(ts.length(password)):
        if password[j] == " ":
            cipher += " "
        elif password[j] in "1234567890":
            cipher += password[j]
        else:
            shift = ord(key[i]) - start
            pos = start + (ord(password[j]) - start + shift) % 26
            cipher += [chr(pos)]

            if i == ts.length(key) - 1:
                i = 0
            else:
                i += 1

    encrypted = ""
    for i in range(ts.length(cipher)):
        encrypted += cipher[i]
    return encrypted


def decrypt(password):
    password = password.lower()
    cipher = []
    start = ord('a')
    key = "tubesdaspro"
    i = 0
    for j in range(ts.length(password)):
        if password[j] == " ":
            cipher += " "
        elif password[j] in "1234567890":
            cipher += password[j]
        else:
            shift = ord(key[i]) + start
            pos = start + (ord(password[j]) + start - shift) % 26
            cipher += [chr(pos)]

            if i == ts.length(key) - 1:
                i = 0
            else:
                i += 1

    decrypted = ""
    for i in range(ts.length(cipher)):
        decrypted += cipher[i]
    return decrypted

# TUBES DASPRO