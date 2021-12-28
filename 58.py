import os
import math

dirname = os.path.dirname(__file__)
filepath1 = os.path.join(dirname, "dane\\58\\dane_systemy1.txt")
filepath2 = os.path.join(dirname, "dane\\58\\dane_systemy2.txt")
filepath3 = os.path.join(dirname, "dane\\58\\dane_systemy3.txt")

s1File = open(filepath1, "r")
s2File = open(filepath2, "r")
s3File = open(filepath3, "r")

S1 = []
S2 = []
S3 = []

for i in s1File.readlines():
    i = i.split(" ")
    S1.append(i)

for i in s2File.readlines():
    i = i.split(" ")
    S2.append(i)

for i in s3File.readlines():
    i = i.split(" ")
    S3.append(i)


def Z1():
    def MinTemperature(S,n):
        minimal = 0
        for x in S:
            if int(x[1], n) < int(minimal):
                minimal = int(x[1], n)
        return bin(minimal).replace("0b", "")

    print(MinTemperature(S1,2))
    print(MinTemperature(S2,4))
    print(MinTemperature(S3,8))


def Z2():
    i = 0
    n = 0
    while i <= 1094:
        if int(S1[i][0], 2) % 12 != 0 and int(S2[i][0], 4) % 12 != 0 and int(S3[i][0], 8) % 12 != 0:
            n += 1
        i += 1
    print(n)
    print(i)

def Z3():
    max1 = int(S1[0][1], 2)
    max2 = int(S2[0][1], 4)
    max3 = int(S3[0][1], 8)
    i = 1
    d = 1
    while i <= 1094:
        if int(S1[i][1], 2) > max1 or int(S2[i][1], 4) > max2 or int(S3[i][1], 8) > max3:
            d += 1
        if int(S1[i][1], 2) > max1:
            max1 = int(S1[i][1], 2)
        if int(S2[i][1], 4) > max2:
            max2 = int(S2[i][1], 4)
        if int(S3[i][1], 8) > max3:
            max3 = int(S3[i][1], 8)
        i += 1
    print("Ostateczne D: ",d)

def Z4():
    i = 0
    j = 1
    leaps = []
    while i <= 1093:
        while j <= 1094:
            leap = math.ceil((math.pow(int(S1[i][1], 2) - int(S1[j][1], 2), 2)) / abs((i+1)-(j+1)))
            leaps.append(leap)
            j += 1
        i += 1
    print(max(leaps))


Z4()
