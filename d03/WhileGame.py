import random as r
ans = r.randint(1, 99)
min, max = 0, 100
while True:
    guess = int(input('請輸入數字 %d ~ %d : ' % (min, max)))
    # 確認所猜的數字是否合理 ?
    if not (guess > min and guess < max):
        print("輸入錯誤, 請重新輸入")
        continue

    # 確認是否有答對 ?
    if(guess < ans):
        min = guess
    elif(guess > ans):
        max = guess
    else:
        print("恭喜答對了")
        break;

