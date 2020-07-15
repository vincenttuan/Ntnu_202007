def f(n):
    if(n < 2):
        return n
    else:
        return f(n-1) + f(n-2)


# 主程式(程式進入點)
if __name__ == '__main__':
    print(f(6))
