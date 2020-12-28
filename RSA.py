from GCD import getGcd
from Inverse import enverseOfNumber
def getPrimeNumber(n):
    rs = n
    while(True):
        for j in range(2, rs+1):
            if(rs % j == 0): break
        if(j == rs): return rs
        rs = rs + 1

def findE(piN):
    for i in range(2,piN) :
        if(getGcd(i, piN) ==1): return i

def generateKey(n):
    p = getPrimeNumber(n)
    q = getPrimeNumber(p)
    p = 23
    q = 67
    n = p*q
    piN = (p-1) * (q-1)
    e = findE(piN)
    d = enverseOfNumber(piN, e)
    return [e, d, n]

def sqareAndMultiply(x, H, n):
    C = 1
    h = "{0:b}".format(H)
    for i in range(len(h)):
        C = C*C % n
        if(h[i] == '1'): 
            C = C * x % n
    return C

P = 65
e = generateKey(20)[0]
d = generateKey(20)[1]
n = generateKey(20)[2]

# C = p^e mod n
C = sqareAndMultiply(P, e , n)
print(C)

# P = C^d mod n
# P = sqareAndMultiply(C, d, n)
# print(P)
