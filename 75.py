file = open("dane/75/tekst.txt")
file2 = open("dane/75/probka.txt")


lista = file.readline().strip().split(" ").copy()
lista2 = [i.strip().split(" ") for i in file2.readlines()]

print(lista)
print(lista2)

def slownik_generator():
    slownik = {}
    j = 0
    for i in range(97,123):
        slownik[chr(i)] = j
        j += 1
    return slownik

def Z1(tekst):
    slowa = []
    for slowo in tekst:
        if slowo[0] == 'd' and slowo[-1] == 'd':
            slowa.append(slowo)

    return slowa

def szyfrowanie(slowo,A,B):
    if 0 <= A and B <= 25:
        alfabet = slownik_generator()
        zaszyfrowane = ""
        for litera in slowo:
            litera = alfabet[litera]
            litera *= A
            litera += B
            if litera > 25:
                litera = litera % 26
            litera = list(alfabet.keys())[list(alfabet.values()).index(litera)]
            zaszyfrowane += litera
        return zaszyfrowane

def Z2(tekst):
    for slowo in tekst:
        if len(slowo) >= 10:
            print(szyfrowanie(slowo,5,2))

def Z3(probka):
    for j in range(26):
        for x in range(26):
            if szyfrowanie(probka[0],j,x) == probka[1]:
                print("Klucz szyfrujący: (",j,",",x,")")

    for j in range(26):
        for x in range(26):
            if szyfrowanie(probka[1],j,x) == probka[0]:
                print("Klucz deszyfrujący: (",j,",",x,")")
    print(" ")


#Z2(lista)
#print(Z1(lista))
for i in range(len(lista2)):
    print("Linia ",i+1)
    Z3(lista2[i])
#print(szyfrowanie('jeden',3,7))


