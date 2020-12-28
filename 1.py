# from fractions import *
# import numpy as np
# # print("hello world")
# # a = 1
# # b = 2
# # c = a
# # c += b
# # print(c)
# # frac = Fraction(4,5)
# # print(frac)
# # strA = "hongdatchy"
# # print(strA)
# # print(strA[-1])
# # print(strA[1:len(strA)])
# # print(strA[1:len(strA)] in strA)
# # print(int("10") + 1)
# # i = 0
# # i += 1
# # print(i)
# # testStr = "abcdef"

# # print(testStr[3 : 6])
# # bitStr = "00111100"
# # print(int(bitStr,2))

# # a = np.array([[1,2], [3,4]]) 

# # print (np.linalg.det(a))
# C = np.array([
#     [1, 0, 2],
#     [2, 7, 3],
#     [10, 7, 1]
# ])

# print(np.linalg.det(C))
# str = "010110"
# a = int("16") << 1
# print(a)
def hex2bin(s): 
    mp = {'0' : "0000",  
          '1' : "0001", 
          '2' : "0010",  
          '3' : "0011", 
          '4' : "0100", 
          '5' : "0101",  
          '6' : "0110", 
          '7' : "0111",  
          '8' : "1000", 
          '9' : "1001",  
          'A' : "1010", 
          'B' : "1011",  
          'C' : "1100", 
          'D' : "1101",  
          'E' : "1110", 
          'F' : "1111" } 
    bin = "" 
    for i in range(len(s)): 
        bin = bin + mp[s[i]] 
    return bin
    
key = "FE01FE01FE01FE01"
shiftKey = key[1:None] + key[0: 1]
print(shiftKey)