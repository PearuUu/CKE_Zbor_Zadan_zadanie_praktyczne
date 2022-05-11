lista1 = [i.strip().split(" ") for i in open("dane/78/podpisy.txt").readlines()]
lista2 = [i.strip() for i in open("dane/78/wiadomosci.txt").readlines()]

# print(lista1)
# print(lista2)

def skrot(wiadomosc):
    napis = "ALGORYTM"
    tablica = [ord(litera) for litera in napis]

    if len(wiadomosc) % 8 != 0:
        roznica = 8 - len(wiadomosc) % 8
        for x in range(roznica):
            wiadomosc += "."
        print("Długość: ",len(wiadomosc))


    for i in range(8,len(wiadomosc)+1, 8):
        fragment = wiadomosc[i-8:i]

        for j in range(len(fragment)):
           tablica[j] = ((tablica[j]) + ord(fragment[j])) % 128

    print(tablica)

    wynik = ""
    for litera in tablica:
        wynik += chr(65 + litera % 26)

    return wynik

def A(d,n, podpis):
    wynik = ""
    for liczba in podpis:
        x = int(liczba)*d % n
        wynik += chr(x)
    return wynik

def Z2(podpisy):
    for podpis in podpisy:
        print(A(3,200,podpis))

def Z3(wiadomosci, podpisy):
    linie = []
    for i in range(len(wiadomosci)):
        if skrot(wiadomosci[i]) == A(3,200,podpisy[i]):
            linie.append(i+1)
    return linie

#print(skrot(lista2[0]))
#Z2(lista1)
print(Z3(lista2,lista1))
