# T = int(input())
# input_data = [list(map(int, input().split())) for __ in range(T)]
# output = [0]*T
# for i in range(T):
#     output[i] = max(0, min(input_data[i][1], input_data[i][3]) - max(input_data[i][0], input_data[i][2]))
# for j in range(T):
#     print(f"#{j+1} {output[j]}")

# T = int(input())
# tunnels = {1: [[1, 0], [0, -1], [-1, 0], [0, 1]], 2: [[1, 0], [-1, 0]], 3: [[0, 1], [0, -1]],
#            4: [[0, 1], [-1, 0]], 5: [[0, 1], [1, 0]],  6: [[1, 0], [0, -1]], 7: [[0, -1], [-1, 0]]}
#
# for tc in range(1, T+1):
#     N, M, R, C, L = map(int, input().split())
#     target = [list(map(int, input().split())) for __ in range(N)]
#     for i in range(L):
#         if i == 0:
#             cur = [[R, C]]
#         else:
#             next = []
#             for pos in cur:
#                 tunnel = target[pos[0]][pos[1]]
#                 if tunnel == 0:
#                     continue
#                 direc = tunnels[tunnel]
#                 for dir in direc:
#                     next_i = pos[0]+dir[0]
#                     next_j = pos[1]+dir[1]
#                     if 0 <= next_i < N and 0 <= next_j < M:
#                         if [next_i, next_j] not in next:
#                             if target[next_i][next_j] and [-dir[0], -dir[1]] in tunnels[target[next_i][next_j]]:
#                                     next.append([next_i, next_j])
#             for j in next:
#                 if j not in cur:
#                     cur.append(j)
#     print(f"#{tc} {len(cur)}")


# def calculate(num, cur):
#     global max_cal, min_cal
#     if num == N-1:
#         if cur > max_cal:
#             max_cal = cur
#             return
#         elif cur < min_cal:
#             min_cal = cur
#             return
#     for i in range(N-1):
#         nxt = 0
#         if used[i]:
#             continue
#         used[i] = 1
#         if cal_list[i] == '+':
#             nxt = cur + target[num+1]
#         elif cal_list[i] == '-':
#             nxt = cur - target[num+1]
#         elif cal_list[i] == '*':
#             nxt = cur * target[num+1]
#         elif cal_list[i] == '/':
#             nxt = int(cur / target[num+1])
#         calculate(num+1, nxt)
#         used[i] = 0


def calculate(num, cur):
    global max_cal, min_cal
    if num == N-1:
        if max_cal is None:
            max_cal = cur
            min_cal = cur
        if cur > max_cal:
            max_cal = cur
            return
        if cur < min_cal:
            min_cal = cur
            return
    for i in range(4):
        nxt = 0
        if not cal_list[i]:
            continue
        cal_list[i] -= 1
        if i == 0:
            nxt = cur + target[num+1]
        elif i == 1:
            nxt = cur - target[num+1]
        elif i == 2:
            nxt = cur * target[num+1]
        elif i == 3:
            nxt = int(cur / target[num+1])
        calculate(num+1, nxt)
        cal_list[i] += 1


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cal_list = list(map(int, input().split()))
    target = list(map(int, input().split()))
    max_cal = None
    min_cal = None
    calculate(0, target[0])
    print(f"#{tc} {max_cal-min_cal}")
