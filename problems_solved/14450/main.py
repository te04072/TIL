T = int(input())
for tc in range(1, T+1):
    L, R, Q = map(int, input().split())
    target = list(map(int, input().split()))
    string = ''
    for i in range(Q):
        temp = target[i]
        temp_L = L
        temp_R = R
        while temp_L or temp_R:         # L과 R의 길이가 다른 케이스가 있을 수 있으므로 and가 아닌 or
            if temp_L <= temp <= temp_R:    # 주어진 숫자가 접두사가 될수 있다면 O
                string += 'O'
                break
            else:
                temp_L //= 10               # R이 0이 될 때까지 끝자리 하나씩 제거
                temp_R //= 10
        else:
            string += 'X'
    print(f"#{tc} {string}")

