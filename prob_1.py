list_3 = []
list_5 = []
list_15 = []
limit_num = 1000
total = 0
for i in range(limit_num):
    num = i
    if num % 3 == 0:
        list_3.append(num)
    if num % 5 == 0:
        list_5.append(num)
    if num % 15 == 0:
        list_15.append(num)
    total += num
print(sum(list_3) + sum(list_5) - sum(list_15))

