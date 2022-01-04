file = open("dane/73/tekst.txt")
plik = file.readline()
lista = plik.strip().split(" ")

#print(lista)

dlugosc = len(plik.strip().replace(" ",""))

def Z1(text):
    suma = 0
    for word in text:
        for i in range(1,len(word)):
            #print(word[i])
            if word[i] == word[i-1]:
                suma += 1
                break
    return suma

def slownik_generator():
    slownik = {}
    for i in range(65,91):
        slownik[chr(i)] = 0
    return slownik

def Z2(text):
    alfabet = slownik_generator()
    for letter in text:
        alfabet[letter] += 1
    for key in alfabet.keys():
        procent = str(round((alfabet[key]/dlugosc)*100,3)) + "%"
        alfabet[key] = str(alfabet[key]) +" ("+ procent +")"
        print(key+": "+alfabet[key])
    return alfabet

def wyznacz_podslowo(slowo):
    samogloski = "AEIOUY"
    podslowo = ""
    curr_podslowo = ""
    for litera in slowo:
        # print("podslowo: ", curr_podslowo)
        # print("litera: ", litera)
        if litera not in samogloski:
            curr_podslowo += litera
        elif len(curr_podslowo) > len(podslowo):
            podslowo = curr_podslowo
            curr_podslowo = ""
        else:
            curr_podslowo = ""
    if len(curr_podslowo) > len(podslowo):
        podslowo = curr_podslowo

    return podslowo
def Z3(text):
    max_podslowo = 0
    liczba_slow = 0
    pierwsze_slowo = ""
    for word in text:
        podslowo_length = len(wyznacz_podslowo(word))
        if podslowo_length > max_podslowo:
            max_podslowo = podslowo_length
    for word in text:
        podslowo_length = len(wyznacz_podslowo(word))
        if podslowo_length == max_podslowo:
            if len(pierwsze_slowo) == 0:
                pierwsze_slowo = word
            liczba_slow += 1
    return max_podslowo, liczba_slow, pierwsze_slowo

#print(Z1(lista))
#Z2(plik.strip().replace(" ",""))
print(Z3(lista))
#print(wyznacz_podslowo('ESTRANGEMENT'))
