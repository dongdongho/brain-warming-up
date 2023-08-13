n = int(input().strip())

arr = []
for i in range(n):
    arr.extend([[0]*n])

current = 1
length = n
for i in range(length//2):
    min_n = i
    max_n = length - (i+1)
    
    pointer = min_n
    while pointer <= max_n:
        print(min_n, pointer)
        arr[min_n][pointer] = current
        current += 1
        pointer += 1

    pointer = min_n + 1
    while pointer <= max_n:
        print(pointer, max_n)
        arr[pointer][max_n] = current
        current += 1
        pointer += 1

    pointer = max_n - 1
    while i <= pointer:
        print(max_n, pointer)
        arr[max_n][pointer] = current
        current += 1
        pointer -= 1

    pointer = max_n - 1
    while i+1 <= pointer:
        print(pointer, min_n)
        arr[pointer][min_n] = current
        current += 1
        pointer -= 1

arr[n//2][n//2] = current
print(arr)

# print(length, n)