import math
import numpy as np
sBox1 = [
    [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
    [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
    [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
    [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]
]
sBox2 = [
    [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
    [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
    [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
    [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]
]
sBox3 = [
    [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
    [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
    [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
    [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]
]
sBox4 = [
    [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
    [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
    [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
    [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]
]
sBox5 = [
    [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
    [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
    [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
    [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]
]
sBox6 = [
    [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
    [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
    [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
    [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]
]
sBox7 = [
    [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
    [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
    [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
    [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]
]
sBox8 = [
    [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
    [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
    [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
    [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]
]
sBox = [sBox1,sBox2,sBox3,sBox4,sBox5,sBox6,sBox7,sBox8]
compessionPBox = [
    [14, 17, 11, 24, 1, 5, 3, 28],
    [15, 6, 21, 10, 23, 19, 12, 4],
    [26, 8, 16, 7, 27, 20, 13, 2],
    [41, 52, 31, 37, 47, 55, 30, 40],
    [51, 45, 33, 48, 44, 49, 39, 56],
    [34, 53, 46, 42, 50, 36, 29, 32]
]

straightPBox = [
    [16, 7, 20, 21, 29, 12, 28, 17],
    [1, 15, 23, 26, 5, 18, 31, 10],
    [2, 8, 24, 14, 32, 27, 3, 9],
    [19, 13, 30, 6, 22, 11, 4, 25]
]

initialMatrix = [
    [58, 50, 42, 34, 26, 18, 10, 2],
    [60, 52, 44, 36, 28, 20, 12, 4],
    [62, 54, 46, 38, 30, 22, 14, 6],
    [64, 56, 48, 40, 32, 24, 16, 8],
    [57, 49, 41, 33, 25, 17, 9, 1],
    [59, 51, 43, 35, 27, 19, 11, 3],
    [61, 53, 45, 37, 29, 21, 13, 5],
    [63, 55, 47, 39, 31, 23, 15, 7]
]

parityDrop = [
    [57, 49, 41, 33, 25, 17, 9, 1],
    [58, 50, 42, 34, 26, 18, 10, 2],
    [59, 51, 43, 35, 27, 19, 11, 3],
    [60, 52, 44, 36, 63, 55, 47, 39],
    [31, 23, 15, 7, 62, 54, 46, 38],
    [30, 22, 14, 6, 61, 53, 45, 37],
    [29, 21, 13, 5, 28, 20, 12, 4]
]

shiftTable = [ 1, 1, 2, 2,  
                2, 2, 2, 2,  
                1, 2, 2, 2,  
                2, 2, 2, 1 ]

expansionPBox = [
    [32, 1, 2, 3, 4, 5],
    [4, 5, 6, 7, 8, 9],
    [8, 9, 10, 11, 12, 13],
    [12, 13, 14, 15, 16, 17],
    [16, 17, 18, 19, 20, 21],
    [20, 21, 22, 23, 24, 25],
    [24, 25, 26, 27, 28, 29],
    [28, 29, 30, 31, 32, 1]
]

finalMatrix = [
    [40, 8, 48, 16, 56, 24, 64, 32],  
    [39, 7, 47, 15, 55, 23, 63, 31],  
    [38, 6, 46, 14, 54, 22, 62, 30],  
    [37, 5, 45, 13, 53, 21, 61, 29],  
    [36, 4, 44, 12, 52, 20, 60, 28],  
    [35, 3, 43, 11, 51, 19, 59, 27],  
    [34, 2, 42, 10, 50, 18, 58, 26],  
    [33, 1, 41, 9, 49, 17, 57, 25]
]

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
      
def bin2hex(s): 
    mp = {"0000" : '0',  
          "0001" : '1', 
          "0010" : '2',  
          "0011" : '3', 
          "0100" : '4', 
          "0101" : '5',  
          "0110" : '6', 
          "0111" : '7',  
          "1000" : '8', 
          "1001" : '9',  
          "1010" : 'A', 
          "1011" : 'B',  
          "1100" : 'C', 
          "1101" : 'D',  
          "1110" : 'E', 
          "1111" : 'F' } 
    hex = "" 
    for i in range(0,len(s),4): 
        ch = "" 
        ch = ch + s[i] 
        ch = ch + s[i + 1]  
        ch = ch + s[i + 2]  
        ch = ch + s[i + 3]  
        hex = hex + mp[ch] 
          
    return hex

def bin2dec(binary):  
    return str(int(binary,2)) 
  
def dec2bin(num):  
    res = bin(num).replace("0b", "") 
    if(len(res)%4 != 0): 
        div = len(res) / 4
        div = int(div) 
        counter =(4 * (div + 1)) - len(res)  
        for _ in range(0, counter): 
            res = '0' + res 
    return res 

def useMatrix(bitStr, matrix):
    rs = ""
    countRow = len(matrix)
    countCol = len(matrix[0])
    for i in range(countRow):
        for j in range(countCol):
            position = matrix[i][j]-1
            rs += bitStr[position]
    return rs

def shiftLeftKey(key, count):
    return key[count:None] + key[0:count]

def add(bit1, bit2):
    rs = ""
    for i in range(len(bit1)):
        if bool(int(bit1[i])) ^ bool(int(bit2[i])):
            rs = rs +  '1'
        else:
            rs = rs +  '0'
    return rs

roundKeys = []

def generateKey(keyHex):
    keyBit = hex2bin(keyHex)
    keyParityDrop = useMatrix(keyBit, parityDrop)
    keyLeft = keyParityDrop[0:28]
    keyRight = keyParityDrop[28:56]
    for i in range(16):    
        keyLeft = shiftLeftKey(keyLeft, shiftTable[i])
        keyRight = shiftLeftKey(keyRight, shiftTable[i])
        keyParityDrop = keyLeft + keyRight
        keyRightCompresion = useMatrix(keyParityDrop, compessionPBox)
        roundKeys.append(bin2hex(keyRightCompresion))

def throughSBox(bit):
    rs = ""
    for i in range(8):
        hangBit = bit[i*6] + bit[i*6+5]
        cotBit = bit[i*6+1] + bit[i*6+2] + bit[i*6+3] + bit[i*6+4]
        hang = int(hangBit, 2)
        cot = int(cotBit, 2)
        sBoxElementBit = "{0:04b}".format(int(str(sBox[i][hang][cot]), 10))
        rs = rs + sBoxElementBit
    return rs

def process(plainTextHex, keyHex, isEncyption):
    generateKey(keyHex)
    plainTextBit = hex2bin(plainTextHex)
    L = [None for x in range(17)]
    R = [None for x in range(17)]
    
    initial = useMatrix(plainTextBit, initialMatrix)
    L[0] = initial[0:32]
    R[0] = initial[32:64]
    for i in range(16):
        print("Round " + str(i+1))
        print("Key: "+ roundKeys[i])
        expansion = useMatrix(R[i], expansionPBox)
        if(isEncyption):
            bitXor = add(expansion, hex2bin(roundKeys[i]))
        else:
            bitXor = add(expansion, hex2bin(roundKeys[15-i]))
        bitSBox = throughSBox(bitXor)
        bitStraightPBox = useMatrix(bitSBox, straightPBox)
        bitMixer = add(bitStraightPBox, L[i])
        R[i+1] = bitMixer
        L[i+1] = R[i]
        print("Left: "+ L[i+1])
        print("Right: "+ R[i+1])
        print("******************************")
    inputFinalRound = R[16]+L[16]
    cipherText =useMatrix(inputFinalRound, finalMatrix)
    return bin2hex(cipherText)

def encryption(plainTextHex, keyHex):
    return process(plainTextHex, keyHex, True)
def decryption(plainTextHex, keyHex):
    return process(plainTextHex, keyHex, False)

# test
keyHex = "FE01FE01FE01FE01" 
plainTextHex = "FE44E3310FD98327"
cipherText = encryption(plainTextHex, keyHex)
print("CipherText: " + cipherText)
print("PlainText: " + decryption(cipherText, keyHex))

# giải mã bản tin cipher text thu được đúng bản tin plain text ban đầu