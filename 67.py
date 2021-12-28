def fibonacci(liczba):
    num1 = 1
    num2 = 1
    current = 1
    for i in range(2,liczba):
        current = num1 + num2
        #print(current)
        num1 = num2
        num2 = current
    return current

def Z1():
    print(fibonacci(10))
    print(fibonacci(20))
    print(fibonacci(30))
    print(fibonacci(40))

def Z2(zakres):
    for i in range(3,zakres+1):
        num = fibonacci(i)
        is_prime = True
        for j in range(2,num):
            if num % j == 0:
                is_prime = False
                break
        if is_prime:
            print(i,".",num)

def Z3(zakres):
    maxlen = 0
    numbers = []
    for i in range(1,zakres+1):
        num = str(bin(fibonacci(i))).replace('0b', "")
        #print("bruh1 ",fibonacci(i))
        #print(num)
        numbers.append(num)
        maxlen = len(num)

    #rint("\n")
    for j in numbers:
        txt = ""
        roznica = maxlen - len(j)
        for x in range(roznica):
            txt += "0"
        txt += j
        for y in txt:
            if y == '0':
                print(" ", end="")
            elif y == '1':
                print(chr(9608), end="")
        print("")
    #print(maxlen)



def Z4(zakres):
    for i in range(1,zakres+1):
        num = fibonacci(i)
        binary = str(bin(num).replace("0b", ""))
        suma = 0
        for j in binary:
            if j == '1':
                suma += 1
        if suma == 6:
            print(binary)

#Z1()
#Z2(40)
Z3(40)

#Z4(40)

