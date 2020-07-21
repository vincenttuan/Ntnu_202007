import requests

file = open('BWIBBU_d.csv', 'r')
data = file.read()

# 資料整理
# "證券代號","證券名稱","殖利率(%)","股利年度","本益比","股價淨值比","財報年/季",
data = data.replace('"-"', '-1')
data = data.replace('"', '')
for d in data.split("\n"):
    list = d.split(",")
    # 表頭
    if list[0] == '證券代號':
        print(list)
    # 表身
    if len(list) == 8 and list[0] != '證券代號':
        # 資料分析
        if float(list[4]) < 10 and float(list[4]) > 0 \
                and float(list[5]) < 1 \
                and float(list[2]) > 7:
            print(list)
