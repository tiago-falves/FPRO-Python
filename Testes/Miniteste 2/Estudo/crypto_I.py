def encrypt(message, cipher):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    encrypted = ''
    for char in message:
        if char == ' ':
            encrypted = encrypted + ' '
        else:
            pos = alphabet.index(char)
            encrypted = encrypted + cipher[pos]
    return encrypted

def decrypt(encrypted, cipher):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    decrypted = ''
    for char in encrypted:
        if char == ' ':
            decrypted = decrypted + ' '
        else:
            pos = cipher.index(char)
            decrypted = decrypted + alphabet[pos]
    return decrypted
a="uzbcadfgehjklminpqrsotvwxy"
b="hello world"
c="xio robj ur u zuxdqemc"
print(decrypt(c,a))
print(encrypt(b,a))
