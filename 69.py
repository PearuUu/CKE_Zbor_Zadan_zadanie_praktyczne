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


print(Z1(lista))

