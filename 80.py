lista = [i.strip() for i in open("dane/80/dane_trojkaty.txt").readlines()]

def czy_prostokatny(a,b,c):
    a,b,c = int(a), int(b), int(c)
    if (a**2 + b**2 == c**2) or (a**2 + c**2 == b**2) or (c**2 + b**2 == a**2):
        return True
    return False

def Z1(trojkaty):
    for i in range(2,len(trojkaty)):
        a = trojkaty[i-2]
        b = trojkaty[i-1]
        c = trojkaty[i]
        if czy_prostokatny(a,b,c):
            print(a,b,c)
            print(" ")

def Z2(trojkaty: list):
    trojkaty = [int(i) for i in trojkaty]
    trojkaty.sort()
    obw_max = 0
    for i in range(2,len(trojkaty)):
        a = trojkaty[i - 2]
        b = trojkaty[i - 1]
        c = trojkaty[i]
        obw = a + b + c
        if c < b:
            c,b = b,c
        if c < a:
            c,a = a,c
        if a+b > c:
            if obw > obw_max:
                obw_max = obw
    return obw_max

def czy_przystajace(trojkat1, trojkat2):
    trojkat1 = [int(i) for i in trojkat1]
    trojkat2 = [int(i) for i in trojkat2]
    is_przystajacy = False

    for i in trojkat1:
        if i in trojkat2:
            is_przystajacy = True
        else:
            is_przystajacy = False
    return is_przystajacy

def Z3(trojkaty: list):
    suma = 0
    ile = 1000
    for i in range(ile-2):
        for j in range(i+1,ile-1):
            for x in range(j+1,ile):
                a = trojkaty[i]
                b = trojkaty[j]
                c = trojkaty[x]
                if (a+b>c) and (a+c>b) and (b+c>a):
                    suma += 1
    return suma

#print(czy_przystajace([10,18,15],[10,18,13]))



#Z1(lista)
#print(Z2(lista))
print(Z3(lista))

