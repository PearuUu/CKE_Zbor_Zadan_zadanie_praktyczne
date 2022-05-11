lista1 = [i.strip().split("\t") for i in open('dane/81/wspolrzedne.txt').readlines()]
lista2 = [i.strip().split("\t") for i in open('dane/81/wspolrzedneTR.txt').readlines()]

print(lista1)
print(lista2)

def czy_icwiartka(wierzcholki):
    for i in wierzcholki:
        i = int(i)
        if i <= 0:
            return False
    return True

def Z1(wspolrzedne):
    suma = 0
    for i in wspolrzedne:
        if czy_icwiartka(i):
            suma += 1
    return suma

def czy_wpolliniowe(wierzcholki):
    wierzcholki = [int(i) for i in wierzcholki]
    AB = abs((wierzcholki[2]-wierzcholki[0])**2 + (wierzcholki[3]-wierzcholki[1])**2)
    AC = abs((wierzcholki[4]-wierzcholki[0])**2 + (wierzcholki[5]-wierzcholki[1])**2)
    BC = abs((wierzcholki[4]-wierzcholki[2])**2 + (wierzcholki[5]-wierzcholki[3])**2)

    if AB == AC + BC:
        print(AB)
        print(AC)
        print(BC)
        return True
    return False

def Z2(wspolrzedne):
    suma = 0
    for i in wspolrzedne:
        print(i)
        if czy_wpolliniowe(i):
            suma += 1
        print(" ")
    return suma

#print(Z1(lista1))
print(Z2(lista1))
