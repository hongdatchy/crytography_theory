def decimalToBinary(n, s):
    rs = str(bin(n)[2:None])
    if len(rs) < s:
        for i in range(s-len(rs)):
            rs = '0' + rs
    return rs
def xorStr(bitStr1, bitStr2, s):
    rs = ""
    for i in range(s):
        if bitStr1[i] == bitStr2[i]:
            rs+= '0'
        else: rs += '1'
    return rs
def swap(S, i ,j):
    temp = S[i]
    S[i] = S[j]
    S[j] = temp
P = [1,2,2,2] #plain text
C = [] #cipher text
# từ k sinh ra T
K = [1,2,3,6]
T= [] 
for i in range(8):
    T.append(K[i%len(K)])
print("T: " + str(T))
# đổi chỗ S
S = [0, 1, 2, 3, 4, 5, 6, 7]
j = 0
for i in range(8):
    j = (j + S[i] + T[i]) % 8
    swap(S, i ,j)
j = 0
i =0
for count in range(4):
    i = (i + 1) % 8
    j = (j + S[i]) % 8
    swap(S, i ,j)
    t = (S[i] + S[j]) % 8
    k = S[t]
    ci = xorStr(decimalToBinary(k,3), decimalToBinary(P[count],3), 3)
    C.append(int(ci,2))
print("plant text:  " + str(P))
print("key:         " + str(K))
print("cipher text: " + str(C))