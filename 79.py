import math

file = open("dane/79/okregi.txt")
okregi = []

for line in file:
    line2 = ""
    prev_char = ""
    for char in line:
        if char != " ":
            if prev_char == " ":
                line2 += " "
            line2 += char

        prev_char = char
    okregi.append(line2.strip().split(" "))


def cwiartka(okrag):
    okrag[0], okrag[1], okrag[2] = float(okrag[0]), float(okrag[1]), float(okrag[2])
    if abs(okrag[0]) > okrag[2] and abs(okrag[1]) > okrag[2]:
        if okrag[0] > 0 and okrag[1] > 0:
            return True, "I"
        elif okrag[0] < 0 and okrag[1] > 0:
            return True, "II"
        elif okrag[0] < 0 and okrag[1] < 0:
            return True, "III"
        elif okrag[0] > 0 and okrag[1] < 0:
            return True, "IV"
    return False, False


def Z1(okregi):
    slownik = {}
    slownik["I"] = 0
    slownik["II"] = 0
    slownik["III"] = 0
    slownik["IV"] = 0
    other = 0
    for okrag in okregi:
        czesc = cwiartka(okrag)
        if czesc[0]:
            slownik[czesc[1]] += 1
        else:
            other += 1

    return slownik, other


def czy_lustrzany(okrag1, okrag2):
    okrag1 = [float(i) for i in okrag1]
    okrag2 = [float(i) for i in okrag2]
    if okrag1 != okrag2:
        if okrag1[2] == okrag2[2]:
            # print(okrag1[1], okrag2[1])
            if (okrag1[0] == -okrag2[0]) or (okrag1[1] == -okrag2[1]):
                if (okrag1[0] == -okrag2[0]) and (okrag1[1] == -okrag2[1]):
                    return False
                return True
        return False
    return False


def Z2(okregi):
    suma = 0
    for i in range(len(okregi)):
        for j in range(i + 1, len(okregi)):
            if czy_lustrzany(okregi[i], okregi[j]):
                suma += 1
    return suma


def czy_prostopadly(okrag1, okrag2):
    okrag1 = [float(i) for i in okrag1]
    okrag2 = [float(i) for i in okrag2]
    if okrag1 != okrag2:
        if okrag1[2] == okrag2[2]:
            if ((okrag1[0] == okrag2[1]) and (okrag1[1] == -okrag2[0])):
                return True
        return False
    return False


def Z3(okregi):
    suma = 0
    for okrag in okregi:
        for okrag2 in okregi:
            # print(okrag)
            # print(okrag2)
            # print(czy_prostopadly(okrag,okrag2))
            # print(" ")
            if czy_prostopadly(okrag, okrag2):
                suma += 1
    return suma


def czy_punkt_wspolny(okrag1, okrag2):
    okrag1 = [float(i) for i in okrag1]
    okrag2 = [float(i) for i in okrag2]
    # print("|R-r|: ", abs(okrag1[2] - okrag2[2]))
    # print("|S1S2|: ", pow(abs(okrag1[2] - okrag2[2]),2))
    # print("R + r: ", pow(okrag1[2] + okrag2[2],2))

    if pow(abs(okrag1[2] - okrag2[2]),2) < pow(okrag2[0]-okrag1[0],2) + pow(okrag2[1]-okrag1[1],2) < pow(okrag1[2] + okrag2[2],2):
        return True
    return False

def Z4(okregi):
    lancuchy = []
    lancuch_len = 1
    for i in range(1,1000):
        print(okregi[i])
        if czy_punkt_wspolny(okregi[i], okregi[i-1]):
            lancuch_len += 1
        else:
            lancuchy.append(lancuch_len)
            lancuch_len = 1
    if lancuch_len != 0:
        lancuchy.append(lancuch_len)
    return lancuchy, max(lancuchy)


# print(Z1(okregi))
# print(Z2(okregi))
# print(Z3(okregi))
print(Z4(okregi))
#print(czy_punkt_wspolny(["8", "5", "40"], ["22", "21","50"]))
