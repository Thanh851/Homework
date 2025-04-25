def bai1():
    numbers = [1,2,3,4,5,6,7,8,9]
    total = sum(numbers)

def bai2():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    total = 1
    for i in numbers:
        total *= i
    print(total)
def bai3():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    largestnumber = max(numbers)
    print(largestnumber)

    print(largestnumber)
def bai4():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    smallestnumber = min(numbers)
    print(smallestnumber)

    print(smallestnumber)

def bai5():
    List = ['abc', 'xyz', 'aba', '1221']
    dem = 0
    for i in List:
        if len(i) >= 2 and i[0] == i[-1]:
            dem += 1
    print(dem)

def bai6():
    SampleList = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
    kq = sorted(SampleList, key= lambda x : x[-1])
    print(kq)


if __name__ == '__main__':
    bai3()