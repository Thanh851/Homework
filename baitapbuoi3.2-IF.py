# Write a program to check a person is eligible for voting or not (saccept age from user)
def ex01():
    age = int(input("Mời bạn nhập số tuổi"))
    if age > 5:
        print("You are eligible for voting")
    else:
        print("You are eligible for voting")

# Write a program to check whether a number entered by user is even or odd.
def ex02():
    number = int(input("Moi ban nhap so"))
    if number % 2 == 0:
         print(f"So {number} la so chan")
    else:
        print(f"So {number} la so le")

def ex03():
    number1= int(input("Moi ban nhap so"))
    if number1 %3 == 0:
         print(f"So {number1}la so chia het cho 3")
    else:
        print(f"So {number1}la so khong chia het cho 3")

def ex04():
    number2 = (input("Moi ban nhap so"))
    number3 =int(number2[-1:])
    if number3 % 3 == 0:
        print(f"So {number3}la so chia het cho 3")
    else:
        print(f"So {number3}la so khong chia het cho 3")

import random
def ex05():
    num = random.randint(a =1, b= 9)
    nums = int(input("Moi ban nhap so"))
    if num == nums:
        print("Thua gia cát lượng mỗi cây quạt")
    else:
        print("Nói khùng nói điên, trả lời lại cho mẹ")

def ex06():
    a = int(input("Moi nhap mot so tu 1 den 7: "))
    if a == 1:
        print("Sunday")
    elif a ==2:
        print("Monday")
    elif a == 3:
        print("Tuesday")
    elif a ==4:
        print("Wednesday")
    elif a ==5:
        print("Thursday")
    elif a ==6:
        print("Friday")
    else:
        print("Saturday")

if __name__ == '__main__':
    ex04()