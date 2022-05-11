file1 = open("dane/77/dokad.txt").readlines()
dokad = []
for line in file1:
    dokad = line.strip().split(" ").copy()


def slownik_generator(r):
    slownik = {}
    j = 0
    if r:
        for i in range(65, 91):
            slownik[j] = chr(i)
            j += 1
        return slownik
    else:
        for i in range(65, 91):
            slownik[chr(i)] = j
            j += 1
        return slownik


def szyfrowanie(slowo, klucz):
    slownik1 = slownik_generator(0)
    slownik2 = slownik_generator(1)

    zaszyfrowany = ""
    i = 0
    for letter in slowo:
        try:
            print("Litera: ",letter)
            litera = slownik1[letter]
            print("litera liczba: ",litera)
            print("i: ",i)
            print((i % len(klucz)))
            print("litera klucza: ", klucz[(i % len(klucz))])
            print("Litera klucza liczba: ",slownik1[klucz[(i % len(klucz))]])
            litera += slownik1[klucz[(i % len(klucz))]]
            print("litera po dodaniu: ", litera)
            print(litera % len(slownik2))
            zaszyfrowany += slownik2[litera % len(slownik2)]
            print(zaszyfrowany)
            i += 1
        except:
            print("bruh")
            zaszyfrowany += letter
    return zaszyfrowany

def Z1():
    zaszyfrowany = ""
    for slowo in dokad:
        zaszyfrowany += " " + szyfrowanie(slowo,"LUBIMYCZYTAC")

    return zaszyfrowany


print(dokad)
#print(szyfrowanie('WAZNE', 'LUBIMYCZYTAC'))
#print(slownik_generator(0))

print(Z1())
# for i in range(128):
#     print(i, chr(i))
