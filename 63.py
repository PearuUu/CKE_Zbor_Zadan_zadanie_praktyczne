file = open("dane/63/ciagi.txt")

ciagi = [i.strip() for i in file.readlines()]

#print(ciagi)

def Z1(liczby):
    cykliczne = []
    for num in liczby:
        if len(num) % 2 == 0:
            w1 = num[0:len(num)//2]
            w2 = num[len(num)//2:]
            if w1 == w2:
                cykliczne.append(num)

    return cykliczne

def Z2(liczby):
    suma = 0
    for num in liczby:
        prev_num = None
        is_good = False
        for digit in num:
            print("prev: ", prev_num)
            print("digit: ",digit)
            if prev_num == None or (digit == '1' and prev_num == '0' or digit == '0' and prev_num == '1' or digit == '0' and prev_num == '0'):
                prev_num = digit
                is_good = True
            else:
                is_good = False
                break
        print(is_good)
        if is_good:
            suma += 1

    return suma

def Z3(liczby):
    suma = 0
    greatest = None
    smallest = None
    for num in liczby:
        czynniki = []
        dzielnik = 2
        original_num = int(num, 2)
        num = int(num, 2)
        #print(num)
        while dzielnik <= num and num >= 1:
            if num % dzielnik == 0:
                #print(dzielnik)
                num = num // dzielnik
                czynniki.append(dzielnik)
            else:
                dzielnik += 1
        if len(czynniki) == 2:
            suma += 1
            if greatest == None or original_num > greatest:
                greatest = original_num
            if smallest == None or original_num < smallest:
                smallest = original_num
    return suma, greatest, smallest

#print(Z1(ciagi))
#print(Z2(ciagi))
print(Z3(ciagi))
