max_num = 4000000
num_1 = 1
num_2 = 2
num_list = [num_1, num_2]
while 1:
    num_1 = num_1 + num_2
    if num_1 < max_num:
        num_list.append(num_1)
    else:
        break
    num_2 = num_1 + num_2
    if num_2 < max_num:
        num_list.append(num_2)
    else:
        break
print(num_list)
print(sum(num_list))
new_list = [f for f in num_list if f % 2 ==0]
print(new_list)
print(sum(new_list))
