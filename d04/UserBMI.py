# 讀取檔案
file = open('user.txt', 'r')
data = file.read()
print(data)

file = open('user.txt', 'r')
list = file.readlines()
print(list)