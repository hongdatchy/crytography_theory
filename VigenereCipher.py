def vigenereCipher(plainText, key):
    keyMain = ""
    while len(keyMain) < len(plainText): 
        keyMain +=key
    keyMain = keyMain[0:len(plainText)]
    rs = ""
    keyMainAicii = []
    for k in keyMain:
        if k.islower():
            keyMainAicii.append(ord(k)-97)
        elif k.isupper():
            keyMainAicii.append(ord(k)-65)
    i = 0
    for p in plainText:
        if p.islower():
            rs += chr((ord(p)-97 + keyMainAicii[i]) % 26 + 97)
        elif p.isupper():
            rs += chr((ord(p)-65 + keyMainAicii[i]) % 26 + 65)
        else :
            rs += p
        i = i+1
    return rs.upper()

