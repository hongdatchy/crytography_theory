def autokeyCipher(plainText, k):
    rs = ""
    for char in plainText:
        if char.islower():
            rs += chr((ord(char)-97 + k) % 26 + 97)
            k = (ord(char)-97) % 26
        elif char.isupper():
            rs += chr((ord(char)-65 + k) % 26 + 65)
            k = (ord(char)-65) % 26
        else :
            rs += char
    return rs
    
# print(autokeyCipher("attackistoday", 12))