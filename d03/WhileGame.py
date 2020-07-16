import random as r
ans = r.randint(1, 99)
min, max = 0, 100
while True:
    guess = int(input('請輸入數字 %d ~ %d : ' % (min, max)))
    if(guess < ans):
        min = guess
    elif(guess > ans):
        max = guess
    else:
        print("恭喜答對了")
        break;

