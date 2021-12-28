file = open("dane/60/liczby.txt")

numbers = [i.strip() for i in file.readlines()]
numbers.sort()
print(numbers)

def Z1(nums):
    lnums = []

    for i in nums:
        if int(i) < 1000:
            lnums.append(i)
    return len(lnums), lnums[-2], lnums[-1]

def Z2(nums):
    for num in nums:
        dividers_sum = 0
        divider = 1
        dividers = []
        while divider <= int(num):
            if int(num) % divider == 0:
                dividers_sum += 1
                dividers.append(divider)
            divider += 1
        if dividers_sum == 18:
            print("Liczba: ",num)
            print("Dzielniki: ", dividers)

def Z3(nums):
    all_dividers = []
    current_geatest = -1
    for num in nums:
        divider = 2
        dividers = []
        while divider <= int(num):
            if int(num) % divider == 0:
                dividers.append(divider)
            divider += 1
        #print(dividers)
        for i in dividers:
            # print("dividers: ", dividers)
            # print("alldividers list: ",all_dividers)
            # print("ALl dividers: ",all_dividers.count(i) == 0)
            # print("divider: ", i)
            if all_dividers.count(i) == 0 and int(num) > current_geatest:
                #print("Prev greatest: ", current_geatest)
                current_geatest =int(num)
                #print("current greatest: ", current_geatest)
            else:
                break
        all_dividers.extend(dividers)
    all_dividers.sort()
    print(all_dividers)
    print(current_geatest)








#print(Z1(numbers))
#Z2(numbers)
#Z3(numbers)


