file = open("dane/68/dane_napisy.txt")

lista = [i.strip().split(" ") for i in file.readlines()]

#print(lista)

def czy_jednolity(napisy):
    for napis in napisy:
        for letter in range(1, len(napis)):
            if napis[letter] != napis[letter-1]:
                return False
    return True

def Z1(napisy):
    suma = 0
    for i in napisy:
        if czy_jednolity(i):
            if i[0] == i[1]:
                suma += 1
    return suma

def is_anagram(napisy):
    litery = 'ABCDEFGHIJ'
    if len(napisy[0]) == len(napisy[1]):
        for litera in litery:
            if napisy[0].count(litera) != napisy[1].count(litera):
                return False
        return True
    return False
def Z2(napisy):
    suma = 0
    for napis in napisy:
        if is_anagram(napis):
            suma += 1
    return suma

def convert_1d(list):
    lista = []
    for i in list:
        for j in i:
            #print(j)
            lista.append(j)
    return lista

# Chyba źle bo w odpowiedziach jest 17
def Z3(napisy):
    lista = [1 for i in napisy]*2
    napisy = convert_1d(napisy)
    print(napisy)
    print(len(lista))
    i = 0
    max_k = 0
    while i < len(napisy):
        if lista[i] == 1:
            lista[i] = 0
            anagramy = []
            anagramy.append(napisy[i])
            k = 0
            for j in range(len(napisy)):
                if is_anagram([napisy[i], napisy[j]]):
                    anagramy.append(napisy[j])
                    lista[j] = 0
            print(anagramy)
            k = len(anagramy)
            if k > max_k:

                max_k = k

            anagramy.clear()
        i += 1
    return max_k


#print(Z1(lista))
#print(Z2(lista))
#print(Z3(lista))