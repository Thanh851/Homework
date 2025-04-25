import random
def createlist(n):
    listt = []
    for i in range(n):
        x = random.randint(1,100)
        listt.append(x)
    return  listt

def daonguocchuoi(n):
    chuoidaonguoc = n[::-1]
    return chuoidaonguoc

def sapxepdanhsach(n):
    danhsachsapxep = sorted(n)
    return danhsachsapxep

def timphantulonnhatvainravitricuoicung(n):
    solonnhat = max(n)
    for i in range(len(n)-1, -1,-1):
        if n[i] == solonnhat:
            return solonnhat, i

def demsoluongphantubanggiatrixnhaptubanphim(n,a):
    solanxuathien = 0
    cacvitrixuathien = []
    for i in range(len(a)):
        if n == a[i]:
            solanxuathien += 1
            cacvitrixuathien.append(i)
    return solanxuathien, cacvitrixuathien

def inravitricacphantulasonguyento(n):
    if n <= 1:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False
    return True
     
def timcacsoduynhat(n):
    danhsachcacsoduynhat = []
    for i in n:
        if n.count(i) == 1:
            danhsachcacsoduynhat.append(i)
    return danhsachcacsoduynhat

def cacgiatritrongmangvasolanxuathien(n):
    danhsach = {}
    for i in n:
        if i in danhsach:
            danhsach[i] += 1
        else:
            danhsach[i] =1
    return danhsach

def menu():
    number = int(input("Mời bạn nhập số phần tử"))
    listtt = createlist(number)
    while True:
        print("""
1. In ra danh sách vừa tạo.
2. In đảo ngược danh sách.
3. Sắp xếp danh sách và in ra danh sách vừa sắp xếp (dùng sorted).
4. tìm phần tử lớn nhất của danh sách và vị trí phần tử lớn nhất cuối cùng.
5. đếm số lượng các phần tử bằng giá trị X nhập từ bàn phím. In ra các vị trí xuất hiện.
6. In ra vị trí các phần tử là số nguyên tố.
7. tìm các số duy nhất (không trùng lặp) trong danh sách.
8. liệt kê các giá trị xuất hiện trong mảng kèm theo số lần xuất hiện của nó.
9. In ra các đoạn con trong danh sách giảm liên tiếp.
10. thoát""")
        answer = input("Mời bạn nhập số để chọn menu")
        if answer == "10":
            break
        elif answer == "1":
            print(listtt)
        elif answer == "2":
            print(daonguocchuoi(listtt))
        elif answer == "3":
            print (sapxepdanhsach(listtt))
        elif answer == "4":
            maxvalue,position = timphantulonnhatvainravitricuoicung(listtt)
            print(f"Giá trị lớn nhất: {maxvalue}, Vị trí cuối cùng: {position}")
        elif answer == "5":
            x = int(input("Mời bạn phần tử muốn đếm"))
            appear, positionn = demsoluongphantubanggiatrixnhaptubanphim(x, listtt)
            print(f"Số lần xuất hiện của phần tử x là {appear}, vị trí xuất hiện{positionn}")
        elif answer == "6":
            vitricacphantulasonguyento = []
            for i in range(len(listtt)):
                if inravitricacphantulasonguyento(listtt[i]):
                    vitricacphantulasonguyento.append(i)
            print (f"vị trí các phần tử là số nguyên tố{vitricacphantulasonguyento}")
        elif answer == "7":
            print(f"Các số duy nhất không trùng lặp {timcacsoduynhat(listtt)}")
        elif answer == "8":
            print(f"Các giá trí xuất hiện trong mảng và số lần xuất hiện của nó {cacgiatritrongmangvasolanxuathien(listtt)}")

        
    


if __name__ == '__main__':
    menu()