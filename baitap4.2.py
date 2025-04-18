import random

def get_gues():
    while True:
        guess = int(input("""Mời bạn đoán:
  1 - Tài (Tổng > 5)
  2 - Xỉu (Tổng <= 5)
  3 - Cược số 5 (Tổng = 5)
""").strip())
        if guess in [1,2,3]:
            return guess
        else:
            print("Vui lòng nhập lại 1,2,3")

def playgame():
    sum = 0
    print("Bạn có 100000 dồng")
    price = 100000

    while True:
        a = random.randint(1,6)
        b = random.randint(1,6)
        total = a + b
        guess = get_gues()
        if guess == 3:
            if total == 5:
                print("Bạn đoán đúng, tổng xúc xắc bằng 5")
                sum += 1
                price += 30000
            else:
                print("Bạn đã đoán sai")
                price -= 10000
        elif guess == 1:
            if total > 5:
                print("Bạn đã đoán đúng là Tài")
                sum += 1
                price += 10000
            else:
                print("Bạn đã đoán sai")
                price -= 10000
        elif guess == 2:
            if total <= 5:
                print("Bạn đã đoán đúng là Xỉu")
                sum += 1
                price += 10000
            else:
                print("Bạn đã đoán sai")
                price -= 10000
        

        if price <= 0:
            print("Bạn đã hết tiền")
            break
        
        answer = input("Bạn có muốn tiếp tục chơi hay không, yes or no").lower().strip()
        if answer == "yes":
            continue
        else:
            break
    
    print("\n🎮 Trò chơi kết thúc!")
    print(f"💵 Tổng số tiền còn lại: {price} VNĐ")
    print(f"🏆 Số ván thắng: {sum}")


if __name__ == "__main__":
    playgame()
        