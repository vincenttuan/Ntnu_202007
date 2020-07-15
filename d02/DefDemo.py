# 請幫我印出 Hello Python
def printHello():  # 此方法為無回傳值方法
    print("Hello Python")

def sum(x, y):  # 此方法為有回傳值方法
    result = x + y
    return result  # 回傳值

printHello()
result = sum(10, 20)
print(result)
