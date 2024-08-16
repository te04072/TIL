from pprint import pprint
# T = int(input())
# for test_case in range(1, T+1):
#     V, E = map(int, input().split())
#     adj_m = [[0]*(V+1) for __ in range(V+1)]
#     for i in range(E):
#         v1, v2 = map(int, input().split())
#         adj_m[v1][v2] = 1
#         adj_m[v2][v1] = 1
#     visited = [0] * (V+1)
#     s, g = map(int, input().split())
#     queue = [s]
#     while queue:
#         cur = queue.pop(0)
#         for next in range(1, V+1):
#             if adj_m[cur][next] == 1 and visited[next] == 0:
#                 queue.append(next)
#                 visited[next] = visited[cur] + 1
#     print(f"#{test_case} {visited[g]}")

# T = int(input())
# for test_case in range(1, T+1):
#     size = int(input())
#     target = [list(map(int, input())) for __ in range(size)]
#     for i in range(size):           # 시작점, 도착점 입력
#         for j in range(size):
#             if target[i][j] == 2:
#                 s = [i, j]
#             elif target[i][j] == 3:
#                 g = [i, j]
#             # target[i][j] *= -1
#     queue = [s]
#     target[s[0]][s[1]] = -1
#     delta = [[1, 0], [0, -1], [-1, 0], [0, 1]]
#     output = 0
#     result = False
#     while queue:
#         cur = queue.pop(0)
#         for k in range(4):
#             next_i = cur[0] + delta[k][0]
#             next_j = cur[1] + delta[k][1]
#             output = -target[cur[0]][cur[1]] - 1
#             if (0 <= next_i < size) and (0 <= next_j < size):
#                 if target[next_i][next_j] == 3:
#                     result = True
#                     break
#                 elif target[next_i][next_j] == 0:
#                     queue.append([next_i, next_j])
#                     target[next_i][next_j] = target[cur[0]][cur[1]] - 1
#         if result:
#             break
#     if result is False:
#         output = 0
#     print(f"#{test_case} {output}")

# DFS
T = int(input())
for test_case in range(1, T+1):
    size = int(input())
    target = [list(map(int, input())) for __ in range(size)]
    for i in range(size):           # 시작점, 도착점 입력
        for j in range(size):
            if target[i][j] == 2:
                s = [i, j]
            elif target[i][j] == 3:
                g = [i, j]
            # target[i][j] *= -1
    stack = [s]
    target[s[0]][s[1]] = -1
    delta = [[1, 0], [0, -1], [-1, 0], [0, 1]]
    output = 0
    result = False
    while queue:
        cur = stack.pop
        for k in range(4):
            next_i = cur[0] + delta[k][0]
            next_j = cur[1] + delta[k][1]
            output = -target[cur[0]][cur[1]] - 1
            if (0 <= next_i < size) and (0 <= next_j < size):
                if target[next_i][next_j] == 3:
                    result = True
                    break
                elif target[next_i][next_j] == 0:
                    stack.append([next_i, next_j])
                    target[next_i][next_j] = target[cur[0]][cur[1]] - 1
        if result:
            break
    if result is False:
        output = 0
    print(f"#{test_case} {output}")


# for test_case in range(1, 11):
#     tc = int(input())
#     size = 16
#     target = [list(map(int, input())) for __ in range(size)]
#     for i in range(size):           # 시작점, 도착점 입력
#         for j in range(size):
#             if target[i][j] == 2:
#                 s = [i, j]
#             elif target[i][j] == 3:
#                 g = [i, j]
#     queue = [s]
#     target[s[0]][s[1]] = 1
#     delta = [[1, 0], [0, -1], [-1, 0], [0, 1]]
#     output = 0
#     result = False
#     while queue:
#         cur = queue.pop(0)
#         for k in range(4):
#             next_i = cur[0] + delta[k][0]                           # delta 4방향 순서대로 확인
#             next_j = cur[1] + delta[k][1]
#             if (0 <= next_i < size) and (0 <= next_j < size):       # 인덱스 범위 이내 확인
#                 if target[next_i][next_j] == 3:                     # 도착지점 발견
#                     output = 1
#                     result = True
#                     break
#                 elif target[next_i][next_j] == 0:
#                     queue.append([next_i, next_j])                  # 가지 않은 곳은 큐에 입력하며 visited 처리
#                     target[next_i][next_j] = 1
#         if result:
#             break
#     print(f"#{test_case} {output}")