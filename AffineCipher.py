from ShiftCipher import shiftCipher
from MultiplicativeCipher import multiplicativeCipher
from MultiplicativeCipher import desMultiplicativeCipher

def affineCipher(plainText, k1, k2):
    rs = multiplicativeCipher(plainText, k1)
    rs = shiftCipher(rs, k2)
    return rs
# print(affineCipher("hello", 7, 2))
    
def desAffineCipher(cipherText, k1, k2):
    rs = shiftCipher(cipherText, -k2)
    if desMultiplicativeCipher(rs, k1) == 0: return 0
    rs = desMultiplicativeCipher(rs, k1)
    return rs
# print(desAffineCipher(affineCipher("hello", 7, 2), 7, 2))