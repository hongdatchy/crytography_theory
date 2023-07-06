from GCD import getGcd

def check(a, b):
    if(getGcd(a,b) == 1): return True
    return False

def inverseOfNumber(r1, r2):
    backUpR1 = r1
    if(check(r1, r2) == False):
        return 0 #tuong ung voi khong co nghich dao nhan
    r = r1 % r2
    q = int(r1 / r2)
    t1 = 0
    t2 = 1
    t = t1 - q * t2
    while(r != 0):
        r1 = r2
        r2 = r 
        q = int(r1 / r2)
        r = r1 % r2
        t1 = t2
        t2 = t
        t = t1 - q * t2
    t2 = t2 % backUpR1
    return t2
# print(inverseOfNumber(26,2039))