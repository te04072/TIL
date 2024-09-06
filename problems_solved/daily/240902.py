# def order(num, current_cost):
#     global min_cost
#
#     # 현재 비용이 이미 최소 비용을 초과하면 탐색 중단
#     if current_cost >= min_cost:
#         return
#
#     if num == N:
#         # 마지막 도시에서 시작 도시로 돌아가는 비용 추가
#         final_cost = current_cost + target[path[-1]][path[0]]
#         min_cost = min(min_cost, final_cost)
#         return
#
#     for i in range(N):
#         if used[i]:
#             continue
#         used[i] = True
#         path.append(i)
#
#         # 다음 도시로 이동하는 비용 계산
#         next_cost = current_cost + (target[path[-2]][i] if num > 0 else 0)
#
#         # 재귀 호출 시 누적 비용 전달
#         order(num + 1, next_cost)
#
#         path.pop()
#         used[i] = False
#
#
# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#     target = [list(map(int, input().split())) for __ in range(N)]
#     path = []
#     used = [False] * N
#
#     # 최소 비용 초기화: 모든 비용의 합으로 설정
#     min_cost = sum(sum(row) for row in target)
#
#     # 초기 비용 0으로 시작
#     order(0, 0)
#     print(f"#{tc} {min_cost}")

# def order(num):
#     if num == 2 * N - 2:
#         route_sum(path)
#     for i in range(2 * N - 2):
#         if used[i]:
#             continue
#         used[i] = True
#         path.append(dir[i])
#         order(num + 1)
#         path.pop()
#         used[i] = False
#
#
# def route_sum(ls):
#     i = 0
#     j = 0
#     sum = target[0][0]
#     global min_sum
#     for k in range(2 * N - 2):
#         i += ls[k][0]
#         j += ls[k][1]
#         sum += target[i][j]
#         if sum >= min_sum:
#             break
#     else:
#         if sum < min_sum:
#             min_sum = sum
#
#
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     target = [list(map(int, input().split())) for __ in range(N)]
#     path = []
#     used = [False]*(2*N-2)
#     dir = [[1, 0], [0, 1]]*(N-1)
#     min_sum = 2000
#     order(0)
#     print(f"#{tc} {min_sum}")



# def prize(ls):
#     money = 0
#     for i in range(len(ls)):
#         money += 10**(len(ls)-i-1)*int(ls[i])
#     return money
#
#
# T = int(input())
# for tc in range(1, T+1):
#     string, N = map(str, input().split())
#     length = len(string)
#     target = [string[i] for i in range(length)]
#     combination = []
#     path = []
#     max_prize = 0
#     maximum = prize(sorted(target, reverse=True))
#     for i in range(length):
#         for j in range(length):
#             if i < j:
#                 combination.append([i, j])
#
#     def exchange(x):
#         global max_prize
#         if x == int(N):
#             new_target = target[:]
#             for k in range(len(path)):
#                 if new_target[path[k][0]] != new_target[path[k][1]]:
#                     new_target[path[k][0]], new_target[path[k][1]] = new_target[path[k][1]], new_target[path[k][0]]
#             if prize(new_target) > max_prize:
#                 max_prize = prize(new_target)
#
#             return
#         for m in range(len(combination)):
#             if target[combination[m][0]] != target[combination[m][1]]:
#                 path.append(combination[m])
#             exchange(x+1)
#             if max_prize == maximum:
#                 return
#             if path:
#                 path.pop()
#
#     exchange(0)
#     print(f"#{tc} {max_prize}")


def order(num):
    global min_cost
    if num == N:
        cost = 0
        for i in range(N):
            if i == N - 1:
                cost += target[path[i]][path[0]]
            else:
                cost += target[path[i]][path[i + 1]]

        if cost < min_cost:
            min_cost = cost
        return

    for i in range(N):
        if used[i]:
            continue
        used[i] = True
        path.append(i)
        order(num + 1)
        path.pop()
        used[i] = False


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    target = [list(map(int, input().split())) for __ in range(N)]
    path = []
    used = [False] * N
    min_cost = 1000
    order(0)
    print(f"#{tc} {min_cost}")