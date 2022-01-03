file = open("dane/69/dane_geny.txt")

lista = [i.strip() for i in file.readlines()]
#print(lista)

def Z1(genotypy):
    max_len = 0
    gen_sum = 0
    lista = [1 for i in genotypy]

    for i in range(len(genotypy)):
        if lista[i] == 1:
            curr_len = 1
            gen_sum += 1
            lista[i] = 0
            for j in range(i+1, len(genotypy)):
                if lista[j] == 0:
                    continue
                else:
                    if len(genotypy[i]) == len(genotypy[j]):
                        curr_len += 1
                        lista[j] = 0
            if curr_len > max_len:
                max_len = curr_len


    print(lista)
    return gen_sum, max_len

def Z1v2(genotypy):
    dlugosci = {}
    for i in genotypy:
        if len(i) not in dlugosci:
            dlugosci[len(i)] = 1
        else:
            dlugosci[len(i)] += 1
    max = 0
    for j in dlugosci.values():
        if j > max:
            max = j

    return len(dlugosci), max

def znajdz_geny(genotyp):
    geny = []
    czy_gen = False
    for i in range(len(genotyp)-1):
        if genotyp[i] == "A" and genotyp[i+1] == "A" and czy_gen == False:
            czy_gen = True
            gen = ""
        elif genotyp[i] == "B" and genotyp[i+1] == "B" and czy_gen == True:
            czy_gen = False
            gen += "BB"
            geny.append(gen)
        if czy_gen:
            gen += genotyp[i]
    return geny



def Z2(genotypy):
    mutacje = 0
    mutacja = "BCDDC"
    for genotyp in genotypy:
        geny = znajdz_geny(genotyp)
        for gen in geny:
            if mutacja in gen:
                mutacje += 1
                break
    return mutacje

def Z3(genotypy):
    max_geny = 0
    max_gen = 0

    for genotyp in genotypy:
        geny = znajdz_geny(genotyp)
        if len(geny) > max_geny:
            max_geny = len(geny)

        for gen in geny:
            if len(gen) > max_gen:
                max_gen = len(gen)

    return max_geny, max_gen

def Z4(genotypy):
    silnie_odporne = 0
    odporne = 0
    for genotyp in genotypy:
        if genotyp == genotyp[::-1]:
            silnie_odporne += 1
            odporne += 1
        elif znajdz_geny(genotyp) == znajdz_geny(genotyp[::-1]):
            odporne += 1
    return odporne, silnie_odporne


#print(Z1(lista))
#print(Z1v2(lista))
#print(Z2(lista))
#print(Z3(lista))
print(Z4(lista))




