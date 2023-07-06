import numpy as np

subWordTable = [
    ["63","7C","77","7B","F2","6B","6F","C5","30","01","67","2B","FE","D7","AB","76"],
    ["CA","82","C9","7D","FA","59","47","F0","AD","D4","A2","AF","9C","A4","72","C0"],
    ["B7","FD","93","26","36","3F","F7","CC","34","A5","E5","F1","71","D8","31","15"],
    ["04","C7","23","C3","18","96","05","9A","07","12","80","E2","EB","27","B2","75"],
    ["09","83","2C","1A","1B","6E","5A","A0","52","3B","D6","B3","29","E3","2F","84"],
    ["53","D1","00","ED","20","FC","B1","5B","6A","CB","BE","39","4A","4C","58","CF"],
    ["D0","EF","AA","FB","43","4D","33","85","45","F9","02","7F","50","3C","9F","A8"],
    ["51","A3","40","8F","92","9D","38","F5","BC","B6","DA","21","10","FF","F3","D2"],
    ["CD","0C","13","EC","5F","97","44","17","C4","A7","7E","3D","64","5D","19","73"],
    ["60","81","4F","DC","22","2A","90","88","46","EE","B8","14","DE","5E","0B","DB"],
    ["E0","32","3A","0A","49","06","24","5C","C2","D3","AC","62","91","95","E4","79"],
    ["E7","C8","37","6D","8D","D5","4E","A9","6C","56","F4","EA","65","7A","AE","08"],
    ["BA","78","25","2E","1C","A6","B4","C6","E8","DD","74","1F","4B","BD","8B","8A"],
    ["70","3E","B5","66","48","03","F6","0E","61","35","57","B9","86","C1","1D","9E"],
    ["E1","F8","98","11","69","D9","8E","94","9B","1E","87","E9","CE","55","28","DF"],
    ["8C","A1","89","0D","BF","E6","42","68","41","99","2D","0F","B0","54","BB","16"]
]
invSubWordTable = [
    ["52", "09", "6A", "D5", "30", "36", "A5", "38", "BF", "40", "A3", "9E", "81", "F3", "D7", "FB"],
    ["7C", "E3", "39", "82", "9B", "2F", "FF", "87", "34", "8E", "43", "44", "C4", "DE", "E9", "CB"],
    ["54", "7B", "94", "32", "A6", "C2", "23", "3D", "EE", "4C", "95", "0B", "42", "FA", "C3", "4E"],
    ["08", "2E", "A1", "66", "28", "D9", "24", "B2", "76", "5B", "A2", "49", "6D", "8B", "D1", "25"],
    ["72", "F8", "F6", "64", "86", "68", "98", "16", "D4", "A4", "5C", "CC", "5D", "65", "B6", "92"],
    ["6C", "70", "48", "50", "FD", "ED", "B9", "DA", "5E", "15", "46", "57", "A7", "8D", "9D", "84"],
    ["90", "D8", "AB", "00", "8C", "BC", "D3", "0A", "F7", "E4", "58", "05", "B8", "B3", "45", "06"],
    ["D0", "2C", "1E", "8F", "CA", "3F", "0F", "02", "C1", "AF", "BD", "03", "01", "13", "8A", "6B"],
    ["3A", "91", "11", "41", "4F", "67", "DC", "EA", "97", "F2", "CF", "CE", "F0", "B4", "E6", "73"],
    ["96", "AC", "74", "22", "E7", "AD", "35", "85", "E2", "F9", "37", "E8", "1C", "75", "DF", "6E"],
    ["47", "F1", "1A", "71", "1D", "29", "C5", "89", "6F", "B7", "62", "0E", "AA", "18", "BE", "1B"],
    ["FC", "56", "3E", "E4", "BC", "D2", "79", "20", "9A", "DB", "C0", "FE", "78", "CD", "5A", "F4"],
    ["1F", "DD", "A8", "33", "88", "07", "C7", "31", "B1", "12", "10", "59", "27", "80", "EC", "5F"],
    ["60", "51", "7F", "A9", "19", "B5", "4A", "0D", "2D", "E5", "7A", "9F", "93", "C9", "9C", "EF"],
    ["A0", "E0", "3B", "4D", "AE", "2A", "F5", "B0", "C8", "EB", "BB", "3C", "83", "53", "99", "61"],
    ["17", "2B", "04", "7E", "BA", "77", "D6", "26", "E1", "69", "14", "63", "55", "21", "0C", "7D"]
]
matrixC = [
    ["02", "03", "01", "01"],
    ["01", "02", "03", "01"],
    ["01", "01", "02", "03"],
    ["03", "01", "01", "02"]
]
rcon = [
    ["01", "00", "00", "00"],
    ["02", "00", "00", "00"],
    ["04", "00", "00", "00"],
    ["08", "00", "00", "00"],
    ["10", "00", "00", "00"],
    ["20", "00", "00", "00"],
    ["40", "00", "00", "00"],
    ["80", "00", "00", "00"],
    ["1B", "00", "00", "00"],
    ["36", "00", "00", "00"]
]
roundKeys = np.array(
    [[[None for x in range(4)] for y in range(4)] for z in range(11)]
    )

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

def xor(hex1, hex2):
    rs = ""
    bit1 = ""
    bit2 = ""
    for i in range(len(hex1)):
        bit1 = bit1 + hex2bin(hex1[i])
        bit2 = bit2 + hex2bin(hex2[i])
    for i in range(len(bit1)):
        if bool(int(bit1[i])) ^ bool(int(bit2[i])):
            rs = rs + '1'
        else: rs = rs + '0'
    return bin2hex(rs)

def add(w1, w2):
    rs = np.array([None for x in range(4)])
    for i in range(len(w1)):
        rs[i] = xor(w1[i], w2[i])
    return rs

def rotWord(row, count):
    rs = [None] * len(row)
    for i in range(len(row)):
        rs[i] = row[(i + count)%len(row)]
    return rs

def subWord(wordRot):
    rs = np.array([None for x in range(4)])
    for i in range(4):
        rs[i] = subWordTable[int(wordRot[i][0], 16)][int(wordRot[i][1], 16)]
    return rs

def generateKey(key):
    words = np.array([[None for x in range(4)] for y in range(44)])
    count = 0
    for i in range(4):
        for j in range(4):
            words[i][j] = key[count: count+2]
            count = count+2
    
    for i in range(4,44):
        if(i%4 == 0):
            wordRot = rotWord(words[i-1], 1)
            wordSub = subWord(wordRot)
            words[i] = (add(add(wordSub, rcon[int((i-4)/4)]), words[i-4]))
        else:
            words[i] = add(words[i-1], words[i-4])
    count = 0
    for i in range(11):
        for j in range(4):
            roundKeys[i][j] = words[count]
            count = count +1
        roundKeys[i] = roundKeys[i].transpose()

def addRoukey(state, roundKey):
    stateAddRoundKey = np.array([[None for x in range(4)] for y in range(4)])
    for i in range(len(state)):
        stateAddRoundKey[i] = add(state[i], roundKey[i])
    return stateAddRoundKey

def subByte(stateAddRoundKey):
    stateSubByte = np.array([[None for x in range(4)] for y in range(4)])
    for i in range(4):
        stateSubByte[i] = subWord(stateAddRoundKey[i])
    return stateSubByte

def shiftRow(stateSubByte):
    rs = np.array([[None for x in range(4)] for y in range(4)])
    for i in range(4):
        rs[i] = rotWord(stateSubByte[i], i)
    return rs

def shift(hex):
    bit = hex2bin(hex)
    rs = bit[1: 8] + "0"
    if(bit[0] == "1"):
        return xor(bin2hex(rs), "1B")
    return bin2hex(rs)

def mutyply(hex1, hex2):
    if(hex1 == "01"): return hex2
    if(hex1 == "02"): return shift(hex2)
    if(hex1 == "03"): return xor(shift(hex2) , hex2)

def mixColumn(stateShiftRow):
    rs = np.array([["00" for x in range(4)] for y in range(4)])
    for i in range(len(matrixC)):
        for j in range(len(stateShiftRow[0])):
            for k in range(len(stateShiftRow)):
                rs[i][j]  = xor(rs[i][j],  mutyply(matrixC[i][k],stateShiftRow[k][j]))
    return rs
                  
def encryption(plantext, key):
    generateKey(key)
    state = np.array([[None for x in range(4)] for y in range(4)])
    count = 0
    for i in range(4):
        for j in range(4):
            state[j][i] = plantext[count: count+2]
            count = count + 2  
    # init round
    state = addRoukey(state, roundKeys[0])
    # 9 round 
    for i in range(1,10):
        state = subByte(state)
        state = shiftRow(state)
        state = mixColumn(state)
        state = addRoukey(state, roundKeys[10-i])
    # final round
    state = subByte(state)
    state = shiftRow(state)
    state = addRoukey(state, roundKeys[10])
    rs = ""
    for i in range(4):
        for j in range(4):
            rs += state[j][i]
    return rs
    
plantext = "54776F204F6E65204E696E652054776F"
key = "5468617473206D79204B756E67204675"

print("cipherText: ")
print(encryption(plantext, key))
state = np.array([
    ["44", "4F", "43", "4F"],
    ["41", "43", "48", "41"],
    ["49", "42", "4B", "48"],
    ["48", "41", "48", "4E"]
])
print(subByte(state))