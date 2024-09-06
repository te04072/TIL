T = int(input())
for tc in range(1, T+1):
    A, B = map(int, input().split())
    M = ((1 << A) - 1) << B                     # 1. 비트연산자로 계산
    N = (1 << (A+B-1)) + ((1 << (A-1))-1)
    num = M * N
    output = 0
    while num:
        if num % 2:
            output += 1
        num //= 2

    # M = 2**(A+B)-2**B                         # 2. 2진수 해석
    # N = 2**(A+B-1)+2**(A-1)-1
    # string = str(bin(M*N))
    # output = 0
    # for i in string:
    #     if i == '1':
    #         output += 1
    print(f"#{tc} {output}")
