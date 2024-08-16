# def DFS_yn(s, g, V):
#     stack = [s]
#     visited = [0] * (V+1)
#     ans = 0
#     while stack:
#         current = stack.pop()
#         if visited[current] == 0:
#             visited[current] = 1
#         for next in range(V, 0, -1):
#             if matrix[current][g] == 1:
#                 ans = 1
#                 break
#             elif matrix[current][next] == 1 and visited[next] == 0:
#                 stack.append(next)
#         if ans == 1:
#             break
#     return ans
#
#
# T = int(input())
# for test_case in range(1, T+1):
#     V, E = map(int, input().split())
#     matrix = [[0]*(V+1) for __ in range(V+1)]
#     for i in range(E):
#         a, b = map(int, input().split())
#         matrix[a][b] = 1        # 방향성 그래프는 전치 x
#     S, G = map(int, input().split())
#     output = DFS_yn(S, G, V)
#     print(f"#{test_case} {output}")


for test_case in range(1, 11):
    tc, E = map(int(input().split()))
    target = [[0]*101 for __ in range(101)]
    visited = [0]*101
    for i in range(E):
        a, b = map(int(input().split()))
        target[a+1][b+1] = 1


