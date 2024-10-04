def solution(dice):
    n = len(dice)
    sum_ls = []
    for i in range(n):
        for j in range(6):
            dice[i][j] **= 0.5
        sum_ls.append([i, sum(dice[i])])
    print(sum_ls)
    for i in range(n-1, -1, -1):
        for j in range(i):
            if sum_ls[j][1] < sum_ls[j+1][1]:
                sum_ls[j], sum_ls[j+1] = sum_ls[j+1], sum_ls[j]
            elif sum_ls[j][1] == sum_ls[j+1][1] and max(dice[sum_ls[j][0]]) < max(dice[sum_ls[j+1][0]]):
                sum_ls[j], sum_ls[j + 1] = sum_ls[j + 1], sum_ls[j]
    print(sum_ls)
    answer = sorted([(sum_ls[k][0] + 1) for k in range(n//2)])
    return answer


# ipt = list(map(int, input().split()) for __ in range(4))
print(solution([[40, 41, 42, 43, 44, 45], [43, 43, 42, 42, 41, 41], [1, 1, 80, 80, 80, 80], [70, 70, 1, 1, 70, 70]]))