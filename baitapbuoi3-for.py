def ex01():
    for i in range(1,11):
        print(i)

def ex02():
    n = int(input("Enter your number"))
    sum_of_numbers = 0
    for i in range(1, n+1):
        sum_of_numbers += i
    print (sum_of_numbers)

def ex03():
    nn = int(input("Enter your number"))
    sum_of_even_numbers = 0
    sum_of_odd_numbers = 0
    for i in range (1, nn +1):
        if i % 2 == 0:
            sum_of_even_numbers += i
        else:
            sum_of_odd_numbers += i
    print(sum_of_odd_numbers,sum_of_even_numbers)

def ex04():
    nguyen_am = 0
    chuoi = (input("Enter your string")).lower()
    for char in chuoi:
        if char in "euoai":
            nguyen_am += 1
    print(nguyen_am)

def ex05():
    chuoi1 = len(input("Enter your string").split())
    print(chuoi1)

def ex06():
    import random
    number_random = random.randint(1,100)
    print(number_random)
    for i in range(1,6):
        chuoi2 = int(input("Mời bạn đoán số từ 1 đến 100"))
        if chuoi2 == number_random:
            print(f"Bạn đã đoán đúng là số{number_random}")
            break
        elif chuoi2 != number_random and i == 5:
            print("Bạn đã hết lượt đoán")
            break
        elif chuoi2 != number_random:
            print(f"Bạn đã đoán sai mời bạn đoán lại, bạn còn {5-i}")
            continue

        


    

if __name__ == '__main__':
    ex06()
