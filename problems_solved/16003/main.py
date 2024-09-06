T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cnt = 0
    cur = 0
    print(f"#{tc}", end=" ")
    while cnt != N and cnt != 50:           # N개 혹은 50개가 나올 때까지 while
        cnt += 1
        if cur and cur*10 <= N:             # 일반적으로는 뒤에 0을 먼저 붙인다
            cur *= 10
        elif cur+1 <= N:                    # 0을 더 붙일 수 없다면 1씩 더한다
            cur += 1
            while not cur % 10:             # 1씩 더해서 끝자리가 0이 되면 10으로 나눈다
                cur //= 10                  # 이후 다음 루프에서 10을 곱하게 된다
        else:
            cur //= 10                      # 이상의 조건들에 해당되지 않으면
            cur += 1                        # 자릿수를 낮추고 1을 더해 다음 숫자로 넘어간다
        if cnt != N and cnt != 50:
            print(f"{cur}.png", end=" ")
        else:
            print(f"{cur}.png")