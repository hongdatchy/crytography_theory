from Inverse import enverseOfNumber

def multiplicativeCipher(plainText, k):
    rs = ""
    for char in plainText:
        if char.islower():
            rs += chr(((ord(char)-97) * k) % 26 + 97)
        elif char.isupper():
            rs += chr(((ord(char))-65 * k) % 26 + 65)
        else :
            rs += char
    return rs

# print(multiplicativeCipher("hello", 7))

# giai ma
def desMultiplicativeCipher(cipherText, k):
    rs = ""
    k = enverseOfNumber(26, k)
    if k == 0: return 0
    for char in cipherText:
        if char.islower():
            rs += chr(((ord(char)-97) * k) % 26 + 97)
        elif char.isupper():
            rs += chr(((ord(char))-65 * k) % 26 + 65)
        else :
            rs += char
    return rs

# print(desMultiplicativeCipher(multiplicativeCipher("hello", 7), 7))
