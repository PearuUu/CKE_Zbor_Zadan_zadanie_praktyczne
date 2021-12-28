liczby1_file = open("dane/62/liczby1.txt")
liczby2_file = open("dane/62/liczby2.txt")

liczby1 = [int(i.strip(), 8) for i in liczby1_file.readlines()]
liczby2 = [int(i.strip()) for i in liczby2_file.readlines()]

#print(liczby1)
print(liczby2)

def Z1(liczby):
    greatest = None
    smallest = None
    for num in liczby:
        if greatest == None or num > greatest:
            greatest = num
        if smallest == None or num < smallest:
            smallest = num
    return oct(greatest), oct(smallest)

def Z2(liczby):
    curr_ciag = []
    longest_ciag = []
    prev_num = None
    for num in liczby:
        if prev_num == None or num >= prev_num:
            curr_ciag.append(num)
            prev_num = num

            # print("dodane")
            # print(curr_ciag)
            # print("longest: ", longest_ciag)

        else:
            #print("else")
            prev_num = None
            #print("len curr: ", len(curr_ciag))
            #print("len longest: ", len(longest_ciag))

            if len(curr_ciag) > len(longest_ciag):
                longest_ciag.clear()
                for i in curr_ciag:
                    longest_ciag.append(i)
                #print("wiekszy")

            #print("longest: ",longest_ciag)
            curr_ciag.clear()
            curr_ciag.append(num)
            #print("longest: ", longest_ciag)

            #print("wyczyszczone")

    return longest_ciag[0], len(longest_ciag)

def Z3(liczby_1, liczby_2):
    equals = 0
    greater = 0
    i = 0
    while i < len(liczby_1):
        if liczby_1[i] == liczby_2[i]:
            equals += 1
        elif liczby_1[i] > liczby_2[i]:
            greater += 1
        i += 1
    return equals, greater

def Z4(liczby):
    in_decimal = 0
    in_octal = 0
    for num in liczby:
        for digit in str(num):
            if digit == '6':
                in_decimal += 1
        for digit in str(oct(num)):
            if digit == '6':
                in_octal += 1
    return in_decimal, in_octal

#print(Z1(liczby1))
#print(Z2(liczby2))
#print(Z3(liczby1, liczby2))
#print(Z4(liczby2))
