T = int(input())
for tc in range(1, T+1):
    N = int(input())
    ans = N
    target = [[]]*N
    for i in range(N):
        target[i] = list(map(int, input().split()))
    target_t = list(map(list, zip(*target)))
    juice = [max(target_t[0]), max(target_t[1]), max(target_t[2])]
    while sum(juice) > 10000:
        r_sum = 0
        r_max = 0
        idx_A = -1
        idx_B = -1
        idx_C = -1
        idx = -1
        for j in range(len(target)):
            if target[j][0] > target[idx_A][0]:
                idx_A2 = idx_A
                idx_A = j
            if target[j][1] > target[idx_B][1]:
                idx_B2 = idx_B
                idx_B = j
            if target[j][2] > target[idx_C][2]:
                idx_C2 = idx_C
                idx_C = j
            temp = sum(target[j])
            if temp > r_sum or (temp == r_sum and max(target[j]) > r_max):
                r_sum = temp
                r_max = max(target[j])
                idx = j
        target[idx] = [0, 0, 0]
        target_t[0][idx] = 0
        target_t[1][idx] = 0
        target_t[2][idx] = 0

        if target[idx_A][0] == 0:
            idx_A = idx_A2
        if target[idx_B][1] == 0:
            idx_B = idx_B2
        if target[idx_C][2] == 0:
            idx_C = idx_C2
        juice = [target[idx_A][0], target[idx_B][1], target[idx_C][2]]
        ans -= 1
    print(f"#{tc} {ans}")