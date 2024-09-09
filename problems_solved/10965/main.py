# 시간 문제 해결 위해 타뷸레이션 사용
T = int(input())
num_list = [1]*T
primes = [2]
max_num = int(10**3.5)
# 입력가능한 최대 수 기준으로 소수 목록 만들기
for i in range(2, max_num+1):
    temp = i
    for j in range(len(primes)):
        while not temp % primes[j]:
            temp //= primes[j]
    if temp != 1:
        primes.append(temp)

for tc in range(T):
    num_list[tc] = int(input())
output = [1]*T
for i in range(T):
    num = num_list[i]
    for j in range(len(primes)):
        if num == 1:
            break
            # 나누는 소수가 더 커지는 시점에서 break
        elif num < primes[j]:
            break
        else:
            # 소수의 제곱으로 나누기. 소인수분해로 매번 output에 약수를 곱하기보다 계산절차가 짧다
            while not num % primes[j]**2:
                num //= primes[j]**2
    output[i] = num
for tc in range(1, T+1):
    print(f"#{tc} {output[tc-1]}")