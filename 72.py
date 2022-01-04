file = open("dane/72/napisy.txt")

lista = [i.strip().split(" ") for i in file.readlines()]

def Z1(tablica):
    suma = 0
    para = []
    for napisy in tablica:
        if len(napisy[0])/3 >= len(napisy[1]) or len(napisy[1])/3 >= len(napisy[0]):
            suma += 1
            if len(para) == 0:
                para.append(napisy[0])
                para.append(napisy[1])
    return suma, para

def czy_dobre(napisy):
    if len(napisy[0]) < len(napisy[1]):
        for i in range(len(napisy[0])):
            if napisy[0][i] != napisy[1][i]:
                return False
        return True
    elif len(napisy[1]) < len(napisy[0]):
        for i in range(len(napisy[1])):
            if napisy[1][i] != napisy[0][i]:
                return False
        return True
    return False

def Z2(tablica):

    for napisy in tablica:
        litery = ""
        roznica = abs(len(napisy[0]) - len(napisy[1]))
        if roznica > 0:
            if czy_dobre(napisy):
                if len(napisy[0]) > len(napisy[1]):
                    litery = napisy[0][len(napisy[1])::]
                elif len(napisy[1]) > len(napisy[0]):
                    litery = napisy[1][len(napisy[0])::]
                print(napisy)
                print(litery)

def koncowki(napisy, length):
    koncowka = ""
    for i in range(length):
        if napisy[0][i] == napisy[1][i]:
            #print(koncowka)
            koncowka += napisy[0][i]
        else:
            return len(koncowka)

def Z3(tablica):
    max_koncowka = 0

    for napisy in tablica:
        min_len = len(min(napisy, key=len))
        napisy[0] = napisy[0][::-1]
        napisy[1] = napisy[1][::-1]
        curr_koncowka = koncowki(napisy, min_len)
        if curr_koncowka > max_koncowka:
            max_koncowka = curr_koncowka
    for napisy in tablica:
        min_len = len(min(napisy, key=len))
        if koncowki(napisy, min_len) == max_koncowka:
            napisy[0] = napisy[0][::-1]
            napisy[1] = napisy[1][::-1]
            print(napisy)
    return max_koncowka

#print(Z1(lista))
#Z2(lista)
print(Z3(lista))




