def factorial(num):
    if num == 1:
        return 1
    else:
        return factorial(num-1)*num


T = int(input())
for tc in range(1, T+1):
    X, Y = map(int, input().split())            # X = 2i + j, Y = i + 2j
    i2 = (2*X - Y)                              # 각각 3i, 3j에 해당
    j2 = (2*Y - X)
    if i2 % 3 or j2 % 3:                        # i2나 j2중 3의 배수가 아닌 것이 있다면 답은 0
        output = 0
    else:
        i2 //= 3                                # 3i, 3j에서 i, j로
        j2 //= 3
        # if i2 == j2:
        #     output = i2+1
        if i2 and j2:                           # i와 j모두 0이 아니라면
            m = max(i2, j2)                     # i와 j를 나열하는 방법은 (m+1)Cn
            n = min(i2, j2)
            temp = n+1
            output = 1
            while temp <= (m+1):
                output *= temp
                temp += 1
            output //= factorial(m+1-n)
            # output = factorial(m+1) // (factorial(n)*factorial(m+1-n))
        else:
            output = 1
    print(f"#{tc} {output}")