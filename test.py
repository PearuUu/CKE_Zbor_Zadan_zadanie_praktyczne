lista = []
obrazek = ""
with open("dane/64/dane_obrazki.txt") as file:
    for line in file:

        if line != "\n" and len(line.strip()) != 20:
            obrazek += line.strip()[:-1]
        else:
            if len(obrazek) > 1:
                lista.append(obrazek)
                obrazek = ""

count = 0
maxi = lista[0].count("1")

for i in lista:
    black = i.count("1")

    if i.count("0") < black:
        count += 1

    if maxi < black:
        maxi = black

print(count, maxi)