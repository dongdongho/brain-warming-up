def is_palindrome(a_b):
    str_a_b = str(a_b)
    len_str = len(str_a_b)
    for idx, c in enumerate(str_a_b):
        comp_idx = len_str - idx - 1
        if c == str_a_b[comp_idx]:
            continue
        else:
            return False
    return True


a = 999
b = 999
max_num = 0
for i in range(901):
    a_i = a - i
    for j in range(901-i):
        b_j = b - j
        mul_val = a_i * b_j
        if is_palindrome(mul_val):
            if max_num < mul_val:
                max_num = mul_val
                print(mul_val)
