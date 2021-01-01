# from fractions import *
import numpy as np
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

# Program to multiply two matrices using nested loops

# 3x3 matrix
X = np.array([[12,7,3],
    [4 ,5,6],
    [7 ,8,9]])
# 3x4 matrix
Y = np.array([[5],
    [6],
    [4]])
# result is 3x4

result = np.array([[0 for x in range(1)] for y in range(3)])
# iterate through rows of X
for i in range(len(X)):
   # iterate through columns of Y
   for j in range(len(Y[0])):
       # iterate through rows of Y
       for k in range(len(Y)):
           result[i][j] += X[i][k] * Y[k][j]


for r in result:
   print(r)
print(X.dot(Y))