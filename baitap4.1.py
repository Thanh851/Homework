import random

def get_level():
    while True:
        level = int(input("""Chọn cấp độ chơi:
  1 - Dễ (9 lần đoán)
  2 - Vừa (6 lần đoán)
  3 - Khó (4 lần đoán)
Nhập 1, 2 hoặc 3: """).strip())
        if level == 1:
            return 9
        elif level == 2:
            return 6
        elif level == 3:
            return 4
        else:
            print("Vui lòng chọn lại cấp độ (1, 2, 3)")

def play_one_game(turns):
    number = random.randint(1, 100)
    for i in range(turns):
        try:
            guess = int(input(f"👉 Lượt {i+1} - Mời bạn đoán số (1-100): ").strip())
        except ValueError:
            print("⚠️ Vui lòng nhập một số nguyên!")
            continue

        if guess < 1 or guess > 100:
            print("⚠️ Chỉ đoán trong khoảng từ 1 đến 100!")
            continue

        if guess == number:
            print("🎉 Chúc mừng! Bạn đã đoán đúng!")
            return True
        elif guess < number:
            print("⬆️ Số bạn đoán nhỏ hơn số bí mật.")
        else:
            print("⬇️ Số bạn đoán lớn hơn số bí mật.")
    
    print(f"😢 Bạn đã hết lượt đoán. Số đúng là: {number}")
    return False

def playgame():
    win = 0
    lose = 0

    while True:
        turns = get_level()
        result = play_one_game(turns)

        if result:
            win += 1
        else:
            lose += 1

        again = input("👉 Bạn có muốn chơi tiếp không? (yes/no): ").lower().strip()
        if again != "yes":
            break

    print("\n🎮 Trò chơi kết thúc!")
    print(f"🏆 Số ván thắng: {win}")
    print(f"💔 Số ván thua: {lose}")

if __name__ == "__main__":
    playgame()
