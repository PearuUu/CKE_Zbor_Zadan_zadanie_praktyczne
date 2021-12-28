file = open("dane/64/bruh.txt")
dane_obrazki = [i.strip() for i in file.readlines()]


print(dane_obrazki)

def Z1(obrazki):
    black = 0
    white = 0
    greatest = 0
    suma = 0
    curr_white = 0
    curr_black = 0
    curr_number = ''
    for i in obrazki:
        curr_number = i
        if len(i) == 0:
            black -= curr_black
            white -= curr_white
            if black > white:
                suma += 1
            if black > greatest:
                greatest = black
            white = 0
            black = 0
            continue
        else:
            curr_black = 0
            curr_white = 0
            for digit in range(len(i) - 1):
                if i[digit] == '0':
                    white += 1
                    curr_white += 1
                elif i[digit] == '1':
                    black += 1
                    curr_black += 1
    else:
        black -= curr_black
        white -= curr_white
        if black > white:
            suma += 1
        if black > greatest:
            greatest = black
        white = 0
        black = 0

    return suma, greatest


# print(Z1(dane_obrazki))

