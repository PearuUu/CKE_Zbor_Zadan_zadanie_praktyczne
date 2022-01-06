file = open("dane/74/hasla.txt")

lista = [i.strip() for i in file.readlines()]

print(lista)

def Z1_czynumery(haslo):
    cyfry = '0123456789'
    for char in haslo:
        if char not in cyfry:
            return False
    return True

def Z1(hasla):
    suma = 0
    for haslo in hasla:
        if Z1_czynumery(haslo):
            suma += 1
    return suma

def Z2(hasla):
    haselka = []
    for i in range(len(hasla)):
        wystapienia = 0

        for j in range(i,len(hasla)):
            #print(hasla[j])
            if hasla[i] == hasla[j]:
                #print("bruh")
                wystapienia += 1

        if wystapienia > 1:
            haselka.append(hasla[i])
            print(" ")
            print(hasla[i])
            print(wystapienia)
            print(haselka)
    return haselka.sort()

def czy_ascii(haslo):
    for i in range(-1,len(haslo)-4):
        fragment = haslo[i + 1::][:4]
        fragment = sorted(fragment)
        if ord(fragment[0]) + 1 == ord(fragment[1]) and ord(fragment[1]) + 1 == ord(fragment[2]) and ord(fragment[2]) + 1 == ord(fragment[3]):
            return True
    return False


def Z3(hasla):
    lista = []
    for haslo in hasla:
        if czy_ascii(haslo):
            lista.append(haslo)

    return len(lista)

def Z4(hasla):
    # for i in range(128):
    #     print(i,": ", chr(i))

    cyfry = [i for i in range(48, 58)]
    d_litery = [i for i in range(65,91)]
    m_litery = [i for i in range(97,123)]

    suma = 0

    for haslo in hasla:
        czy_cyfra = False
        czy_litera_d = False
        czy_litera_m = False

        for litera in haslo:
            if ord(litera) in cyfry:
                czy_cyfra = True
            elif ord(litera) in d_litery:
                czy_litera_d = True
            elif ord(litera) in m_litery:
                czy_litera_m = True

        if czy_cyfra and czy_litera_m and czy_litera_d:
            suma += 1

    return suma


# print(Z1(lista))
# print(Z2(lista))
# print(Z3(lista))
#print(Z4(lista))

