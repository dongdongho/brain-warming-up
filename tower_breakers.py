def largest_proper_divisor(n):
    for i in range(n // 2, 0, -1):
        if n % i == 0:
            return i
    return 1  # 이 경우는 n이 1일 때만 발생합니다.

n = int(input("정수를 입력하세요: "))
divisor = largest_proper_divisor(n)

print(f"{n}의 자기 자신을 제외한 최대 약수는 {divisor}입니다.")
