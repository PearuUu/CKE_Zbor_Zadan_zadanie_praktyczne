import math

file = open("dane/71/funkcja.txt")
lista = []

for line in file:
    line = line.strip().split(chr(32))
    listka = []
    for part in line:
        try:
            part = float(part)
            listka.append(part)
        except:
            continue
    lista.append(listka)

print(lista)

def f(x):
    i = None
    if 0 <= x < 1:
        i = 0
    elif 1 <= x < 2:
        i = 1
    elif 2 <= x < 3:
        i = 2
    elif 3 <= x < 4:
        i = 3
    elif 4 <= x < 5:
        i = 4

    wynik = lista[i][0] + lista[i][1]*x + lista[i][2]*(x**2) + lista[i][3]*(x**3)
    return round(wynik,5)

def Z2():
    i = 0
    max_val = 0
    max_x = 0
    while i < 5:
        i = round(i, 3)
        val = f(i)
        if val > max_val:
            max_val = val
            max_x = i
        i += 0.001
    return max_x, max_val

def Z3():
    i = 0
    miejsca = []
    while i < 5:
        #print(f(i))
        if -0.00001 <= f(i) <= 0.00001:
            print(i)
            miejsca.append(round(i,5))
        i += 0.00001
    return miejsca
#print(f(1.5))
#print(Z2())
print(Z3())
print(f(0.53657))




