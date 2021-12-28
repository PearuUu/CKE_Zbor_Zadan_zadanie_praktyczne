file = open("dane/61/ciagi.txt")
bledne = open("dane/61/bledne.txt")


lines = [i.strip() for i in file.readlines()]
bledne_arr = [i.strip() for i in bledne.readlines()]
#print(lines)

def Z1(ciagi):
    arytmetyczne = []
    greatest = None
    greatest_roz = 0

    for ciag in ciagi:
        if len(ciag) > 4:
            ciag = ciag.split(" ")
            r = int(ciag[1]) - int(ciag[0])
            i = 1
            is_aritmetic = False
            while i < len(ciag):
                if int(ciag[i]) - int(ciag[i-1]) == r:
                    is_aritmetic = True
                    i += 1
                else:
                    is_aritmetic = False
                    break
            if is_aritmetic:
                arytmetyczne.append(ciag)
                if r > greatest_roz:
                    greatest_roz = r
                    greatest = ciag
        else:
            continue
    return len(arytmetyczne), greatest_roz

def Z2(ciagi):
    liczby = []
    for ciag in ciagi:
        greatest = 0
        if len(ciag) > 4:
            ciag = ciag.split(" ")
            for num in ciag:
                podstawa = 1
                szescian = podstawa*podstawa*podstawa

                while szescian <= int(num):
                    szescian = podstawa * podstawa * podstawa
                    if szescian == int(num) and int(num) > greatest:
                        greatest = int(num)
                    podstawa += 1
            if greatest != 0:
                liczby.append(greatest)
        else:
            continue
    return liczby

def Z3(ciagi):
    bledne = []
    for ciag in ciagi:
        if len(ciag) > 4:
            #print(ciag)
            ciag = ciag.split(" ")
            r = int(ciag[1]) - int(ciag[0])
            i = 1

            while i < len(ciag):
                if int(ciag[i]) - int(ciag[i - 1]) != r:
                    bledne.append(ciag[i])
                    break
                i += 1

    return bledne

#print(Z1(lines))
#print(Z2(lines))
#print(Z3(bledne_arr))