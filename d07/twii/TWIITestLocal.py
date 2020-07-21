import requests

file = open('BWIBBU_d.csv', 'r')
data = file.read()

# 資料整理
# "證券代號","證券名稱","殖利率(%)","股利年度","本益比","股價淨值比","財報年/季",
data = data.replace('"-"', '-1')
data = data.replace('"', '')
for d in data.split("\n"):
    list = d.split(",")
    if len(list) == 8:
        print(d)
