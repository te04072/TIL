for test_case in range(1, 11):
    T = int(input())
    building = list(map(int, input().split()))
    ans = 0
    for i in range(2, T-2):
        sample = building[i-2:i+3]
        sample.sort(reverse=True)
        if sample[0] == building[i]:
            ans += sample[0] - sample[1]

    print(f'#{test_case} {ans}')
