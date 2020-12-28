def getGcd(a, b):
    while b!=0:
        r = a % b
        a=b
        b=r
    return a

# print(getGcd(6,9))