import json
data = '[{"name":"John", "age":28, "salary":60000},{"name":"Mary", "age":25, "salary":80000}]'  # 字串格式
user = json.loads(data)  # 轉成 Python 的 list 格式
print(data, type(data))
print(user, type(user))
