import random

def guess_number():
    print("=====================================")
    print("欢迎来到猜数字游戏！")
    print("我已经想好了一个 1 到 100 之间的数字。")
    print("=====================================")
    
    secret_number = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            guess = int(input("请输入你猜的数字: "))
            attempts += 1

            if guess < secret_number:
                print("太小了！再往上猜猜。")
            elif guess > secret_number:
                print("太大了！再往下猜猜。")
            else:
                print(f"\n🎉 恭喜你，猜对了！答案就是 {secret_number}。")
                print(f"你一共猜了 {attempts} 次。")
                break
        except ValueError:
            print("⚠️ 请输入有效的数字！")

if __name__ == "__main__":
    guess_number()

