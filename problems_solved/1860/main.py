T = int(input())
for test_case in range(1, T+1):
    N, M, K = map(int, input().split())             # 손님수, 소요시간, 시간당 붕어빵수
    customers = list(map(int, input().split()))
    ans = "Possible"
    i = 0
    rest = 0
    time = 0
    size = 11112
    count = [0]*size
    for i in range(N):                              # 카운트 리스트 생성
        count[customers[i]] += 1
    for j in range(1, size):
        count[j] += count[j-1]
    for t in range(11112):                              # 누적 붕어빵과 t 시점의 손님수 대소비교
        if t // M * K < count[t]:
            ans = "Impossible"
            break
        if count[t] == N:                               # 손님 n명 다 받으면 break
            break
    print(f"#{test_case} {ans}")