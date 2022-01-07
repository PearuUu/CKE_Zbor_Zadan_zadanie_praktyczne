file1 = open('dane/76/szyfr1.txt').readlines()
klucz1 = file1[-1].split(" ")
napisy1 = [i.strip() for i in file1[:-1]]

file2 = open('dane/76/szyfr2.txt').readlines()
klucz2 = file2[-1].split(" ")
napisy2 = [i.strip() for i in file2[:-1]]

file3 = open('dane/76/szyfr3.txt').readlines()
napisy3 = [i.strip() for i in file3]


print(klucz1)

def szyfrowanie(napis, klucz):
    zaszyfrowany = ""
    if len(napis) >= len(klucz):
        for i in range(len(napis)):
            # print('i: ',i)
            # print("bruh1: ",i%len(klucz))
            klucz_num = int(klucz[i%len(klucz)])
            #print("klucz: ",klucz_num)
            napis = list(napis)
            #print(napis)
            napis[i], napis[klucz_num-1] = napis[klucz_num-1], napis[i]

        for letter in napis:
            zaszyfrowany += letter
        return zaszyfrowany

def deszyfrowanie(napis, klucz):
    zaszyfrowany = ""
    klucz_de = []
    j = len(napis)-1
    if len(napis) >= len(klucz):
        for j in range(len(napis)):
            klucz_de.append(int(klucz[j % len(klucz)]))

        klucz_de = klucz_de[::-1]
        print(klucz_de)
        napis = list(napis)
        for i in range(len(napis)):
            # print('i: ',i)
            # print("bruh1: ",i%len(klucz))
            klucz_num = klucz_de[i]
            print("klucz: ",klucz_num)

            # print(napis)
            napis[j], napis[klucz_num - 1] = napis[klucz_num - 1], napis[j]
            j -= 1
        for letter in napis:
            zaszyfrowany += letter
        return zaszyfrowany

def Z1(napisy, klucz):
    for napis in napisy:
        print(szyfrowanie(napis,klucz))

def Z3(napisy, klucz):
    for napis in napisy:
        print(deszyfrowanie(napis,klucz))

# Z1(napisy1,klucz1)
# Z1(napisy2,klucz2)
# Z3(napisy3,[6,2,4,1,5,3])
