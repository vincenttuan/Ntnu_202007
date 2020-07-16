import random as r
d1 = [1, 2, 3, 4, 5, 6]
d2 = [1, 2, 3, 4, 5, 6]
d3 = [1, 2, 3, 4, 5, 6]

pc_sum   = d1[r.randint(0, 5)] + d2[r.randint(0, 5)] + d3[r.randint(0, 5)]
user_sum = d1[r.randint(0, 5)] + d2[r.randint(0, 5)] + d3[r.randint(0, 5)]
print(pc_sum, user_sum)