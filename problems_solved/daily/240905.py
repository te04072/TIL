# def order(num, cur_cost):
#     global min_sum
#     if num == N:
#         if cur_cost < min_sum:
#             min_sum = cur_cost
#             return
#     if cur_cost > min_sum:
#         return
#     for i in range(N):
#         if used[i]:
#             continue
#         used[i] = True
#         path.append(i)
#         next_cost = cur_cost + target[num][i]
#         order(num+1, next_cost)
#         path.pop()
#         used[i] = False
#
#
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     target = [list(map(int, input().split())) for __ in range(N)]
#     path = []
#     used = [False]*N
#     min_sum = 1500
#     order(0, 0)
#     print(f"#{tc} {min_sum}")


# def dfs(num, p):
#     global final_p
#     if num == N:
#         if p > final_p:
#             final_p = p
#             return
#     if p <= final_p:
#         return
#     for i in range(N):
#         if used[i]:
#             continue
#         used[i] = 1
#         next_p = p*target[num][i]/100
#         dfs(num+1, next_p)
#         used[i] = 0
#
#
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    target = [list(map(int, input().split())) for __ in range(N)]
    final_p = 0
    used = [0]*N
    dfs(0, 1)
    final_p *= 100
    print(f"#{tc} {final_p:.6f}")


T = int(input())
for tc in range(1, T+1):
    target = list(map(int, input().split()))
    N = target[0]
    cur = 1
    cnt = 0
    for i in range(1, N):
        if cur > i:
            continue
        length = target[cur]
        if cur + length >= N:
            break
        next_i = 1
        range_end = min(N-1, cur+length)
        for j in range(cur+1, range_end+1):
            temp = j+target[j]
            if temp > next_i+target[next_i]:
                next_i = j
        cur = next_i
        cnt += 1
    print(f"#{tc} {cnt}")
