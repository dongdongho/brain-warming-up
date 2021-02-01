import time
import math

## 에라토스테네스의 체
target_num = 600851475143 


def is_soinsoo(_num, insoo_list):
    for insoo in insoo_list:
        if _num % insoo == 0:
            return False
    return True
start_time = time.time()
insoo_list = []
result_list = []
for i in range(2, int(math.sqrt(target_num/2))):
    if is_soinsoo(i, insoo_list):
        if target_num % i == 0:
            if is_soinsoo(i, insoo_list):
               result_list.append(i)
            insoo_list.append(i)
print(result_list)
print(time.time() - start_time)
