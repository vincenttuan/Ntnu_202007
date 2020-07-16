emps = {"Tom": 70000, "John": 100000, "Mary": 90000}
print(emps['Tom'])
for key in emps:
    print(key, emps[key])

# 平均薪資
sum = 0
for key in emps:
    salary = emps[key]
    sum += salary
print(sum, sum/len(emps))