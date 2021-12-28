file = open("dane/65/dane_ulamki.txt")

ulamki = [i.strip().split(" ") for i in file.readlines()]

print(ulamki)


def Z1(lista):
    minimum = int(lista[0][0]) / int(lista[0][1])
    # print(minimum)
    index = 0
    minimum_index = 0
    for i in lista:
        number = int(i[0]) / int(i[1])

        if number < minimum:
            # print("i ", i)
            # print("number ", number)
            # print("index ",index)
            minimum = number
            minimum_index = index
            # print(" ")
        elif number == minimum:
            # print("minimum ", lista[minimum_index])
            # print("i ", i)
            # print("number ", number)
            # print("index ", index)

            if int(lista[minimum_index][1]) > int(i[1]):
                minimum = number
                minimum_index = index
                print("zmienieone")
            # print(" ")

        index += 1

    # print("index_minimum ",minimum_index)
    return lista[minimum_index]


def Z2(lista):
    suma = 0
    for i in lista:
        czy_podzielna = False
        for j in range(2, int(i[0]) + 1):
            if int(i[0]) % j == 0 and int(i[1]) % j == 0:
                czy_podzielna = True
                break
        if czy_podzielna == False:
            suma += 1
    return suma


def Z3(lista):
    suma = 0
    for i in lista:
        j = 2
        print("j ", j)
        print("int ", int(i[0]))
        print("bez konwertowaniea: ", i)
        while j <= int(float(i[0])):
            print("bruh", j)
            if int(i[0]) % j == 0 and int(i[1]) % j == 0:
                i[0] = str(int(i[0]) // j)
                i[1] = str(int(i[1]) // j)
                j = 1
                print("dzieleneie", i)
            j += 1
        suma += int(i[0])
    return suma

def Z4(lista):
    b = 2**2 * 3**2 * 5**2 * 7**2 * 13
    suma = 0
    for i in lista:
        suma += (int(i[0])*b)/int(i[1])

    return int(suma)
# print(Z1(ulamki))
# print(Z2(ulamki))
#print(Z3(ulamki))
print(Z4(ulamki))
#print(1/2 + 1/4)