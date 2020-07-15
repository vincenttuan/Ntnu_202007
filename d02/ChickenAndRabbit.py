'''
總隻數 83 總腳數 240
83 * 2 = 166 假設都是雞
240 - 166 = 74 這是兔子假扮的
74 / 2 = 37 (兔子)
83 - 37 = 46 (雞)
'''
def getChickenAndRabbit(amount, feet):
    x = amount * 2  # 假設都是雞
    if (feet < x):
        return None
    y = feet - x    # 這是兔子假扮的
    rabbit = y / 2  # 兔子個數
    return amount-rabbit, rabbit

print(getChickenAndRabbit(83, 240))
print(getChickenAndRabbit(83, 300))