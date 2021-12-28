file = open("dane/66/trojki.txt")

lista = [i.strip().split(" ") for i in file.readlines()]

#print(lista)

def czy_pierwsza(liczba):
    if liczba > 1:
        divider = 2
        while divider**2 <= liczba:
            if liczba % divider == 0:
                return False
            divider += 1
        return True
    return False

def Z1(trojki):
    list = []
    for i in trojki:
        suma = 0
        for digit in i[0]:
            print(digit)
            suma += int(digit)
        print(suma)
        for cyfra in i[1]:
            print(cyfra)
            suma += int(cyfra)
        print(suma)
        if suma == int(i[2]):
            list.append(i)
    return list

def Z2(trojki):
    lista = []
    for i in trojki:
        if czy_pierwsza(int(i[0])) and czy_pierwsza(int(i[1])):
                if int(i[0])*int(i[1]) == int(i[2]):
                    lista.append(i)
    return lista

def Z3(trojki):
    for i in range(1,len(trojki)):
        placeholder1 = trojki[i]
        placeholder2 = trojki[i-1]

        placeholder1 = [int(j) for j in trojki[i]]
        placeholder2 = [int(j) for j in trojki[i-1]]
        placeholder1.sort()
        placeholder2.sort()
        #print(trojki[i])
        #print(trojki[i-1])
        if int(placeholder1[0])**2 + int(placeholder1[1])**2 == int(placeholder1[2])**2:
            #print("bruh")
            if int(placeholder2[0]) ** 2 + int(placeholder2[1]) ** 2 == int(placeholder2[2]) ** 2:
                print(trojki[i-1])
                print(trojki[i])
#print(Z1(lista))
#print(Z2(lista))
Z3(lista)

