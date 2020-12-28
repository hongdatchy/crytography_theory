def shiftCipher(plainText, k):
    rs = ""
    for char in plainText:
        if char.islower():
            rs += chr((ord(char)-97 + k) % 26 + 97)
        elif char.isupper():
            rs += chr((ord(char)-65 + k) % 26 + 65)
        else :
            rs += char
    return rs

# print(shiftCipher("Khoor zruog!", -3))