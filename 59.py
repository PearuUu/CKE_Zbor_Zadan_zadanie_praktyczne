file = open("dane/59/liczby.txt")

lines = []
for num in file.readlines():
    lines.append(int(num))

print(lines)


def Z1(numbers):
    wynik = 0
    for i in numbers:
        czynniki = []
        czynnik = 3
        ile_czynnikow = 0
        pre_czynnik = 0
        if i % 2 == 0:
            continue
        else:
            while czynnik * czynnik <= i:
                if i % czynnik:
                    czynnik += 1
                else:
                    czynniki.append(czynnik)
                    print(i)
                    print(czynnik)
                    i //= czynnik
                    if czynnik != pre_czynnik:
                        ile_czynnikow += 1
                    pre_czynnik = czynnik

            if i > 1:
                print(i)
                czynniki.append(i)
                if i != pre_czynnik:
                    ile_czynnikow += 1
            if ile_czynnikow == 3:
                wynik += 1
    return wynik


def Z2(numbers):
    ile_plaindrom = 0
    for i in numbers:
        i = str(i)
        suma = int(i) + int(i[::-1])
        suma = str(suma)

        if suma[::-1] == suma:
            ile_plaindrom += 1
    return ile_plaindrom


def Z3(number, moc=0):
    if len(str(number)) == 1:
        return moc
    else:
        number = str(number)
        n = int(number[0])

        #print("n: ", n)
        for i in number[1:]:
            # print("i: ", i)
            # print("n: ", n)
            n *= int(i)
        return Z3(n, moc + 1)


def Z_3():
    ile_ilczb = 0
    moc1 = []
    moc2 = []
    moc3 = []
    moc4 = []
    moc5 = []
    moc6 = []
    moc7 = []
    moc8 = []

    for number in lines:
        moc = Z3(number)
        print(moc)
        if moc == 1:
            moc1.append(number)
        if moc == 2:
            moc2.append(number)
        if moc == 3:
            moc3.append(number)
        if moc == 4:
            moc4.append(number)
        if moc == 5:
            moc5.append(number)
        if moc == 6:
            moc6.append(number)
        if moc == 7:
            moc7.append(number)
        if moc == 8:
            moc8.append(number)
    print("Moc 1: ", len(moc1))
    print("Moc 2: ", len(moc2))
    print("Moc 3: ", len(moc3))
    print("Moc 4: ", len(moc4))
    print("Moc 5: ", len(moc5))
    print("Moc 6: ", len(moc6))
    print("Moc 7: ", len(moc7))
    print("Moc 8: ", len(moc8))
    print("Maksymalna liczba o mocy 1: ", max(moc1))
    print("Minimalna liczba o mocy 1: ", min(moc1))

# print("Wynik1: " ,Z1(lines))
# print("Wynik2: " ,Z2(lines))
Z_3()


