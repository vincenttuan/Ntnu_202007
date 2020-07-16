emps = {"Tom": 70000, "John": 100000, "Mary": 90000}

# 薪資最高
name, max = '', 0
for key in emps:
    salary = emps[key]
    if salary > max:
        name = key
        max = salary
print(name, max)


print(emps['Tom'])
for key in emps:
    print(key, emps[key])

# 平均薪資
sum = 0
for key in emps:
    salary = emps[key]
    sum += salary
print(sum, sum/len(emps))


