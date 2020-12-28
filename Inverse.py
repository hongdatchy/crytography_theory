from GCD import getGcd

def check(a, b):
    if(getGcd(a,b) == 1): return True
    return False

def enverseOfNumber(r1, r2):
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
    
# print(enverseOfNumber(26, 2039))

# import numpy as np
# print(7%3)
# print(1%3)
# print(getGcd(24, 60))
# A = np.array(
#     [[1, 4, 5],
#     [-5, 8, 9],
#     [-6, 7, 11]])
# detA = np.linalg.det(A) 
# print(len(A[0]))
# B = A
# B[0][0] =0 
# print(B)
# def getMultiplyEnverseMatrix(A, n):
#     detA = np.linalg.det(A) 
#     if(check(detA, n) == False): return "khong co ma tran nghich dao"
#     B = A
#     B