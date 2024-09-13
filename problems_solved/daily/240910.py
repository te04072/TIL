# def make_set(n):
#     p = [i for i in range(n)]
#     r = [0] * n
#     return p, r
#
#
# def find_set(x):
#     if parents[x] == x:
#         return x
#
#     parents[x] = find_set(parents[x])
#     return parents[x]
#
# def union(x, y):
#     root_x = find_set(x)
#     root_y = find_set(y)
#
#     if root_x == root_y:
#         return
#
#     if ranks[root_x] > ranks[root_y]:
#         parents[root_y] = root_x
#     elif ranks[root_x] < ranks[root_y]:
#         parents[root_x] = root_y
#     else:
#         parents[root_y] = root_x
#         ranks[root_x] += 1
#
# n = 7
# parents, ranks = make_set(n)
# print(parents)
# union(1, 3)
# print(parents)
# union(2, 3)
# print(parents)
# union(5, 6)
# print(parents)
# print('find_set(6) = ', find_set(6))
# print(ranks)
#
# target_x = 3
# target_y = 4
# if find_set(target_x) == find_set(target_y):
#     print("same set")
# else:
#     print("different set")


# def dfs(node):
#     global cnt
#     for nxt in graph[node]:
#         if visited[nxt]:
#             continue
#         visited[nxt] = 1
#         dfs(nxt)
#
#
# T = int(input())
# for tc in range(1, T+1):
#     N, M = map(int, input().split())
#     target = list(map(int, input().split()))
#     graph = [[] for __ in range(N+1)]
#     visited = [0]*(N+1)
#     cnt = 0
#     for i in range(M):
#         graph[target[i*2]].append(target[1+i*2])
#         graph[target[1+i*2]].append(target[i*2])
#     for j in range(1, N+1):
#         if not visited[j]:
#             dfs(j)
#             cnt += 1
#     print(f"#{tc} {cnt}")


# for tc in range(1, 11):
#     length, start = map(int, input().split())
#     ipt = list(map(int, input().split()))
#     adj_matrix = [[0]*101 for __ in range(101)]
#     cnt = 1
#     visited = [0]*101
#     for i in range(length//2):
#         adj_matrix[ipt[i*2]][ipt[1+i*2]] = 1
#     current = [start]
#     visited[start] = 1
#     maximum = 0
#     while current:
#         nxt = []
#         cnt += 1
#         for cur in current:
#             for j in range(101):
#                 if adj_matrix[cur][j] and not visited[j]:
#                     visited[j] = cnt
#                     nxt.append(j)
#         if nxt:
#             maximum = max(nxt)
#         current = nxt[:]
#     print(f"#{tc} {maximum}")


# def make_set(n):
#     p = [i for i in range(n)]
#     r = [0] * n
#     return p, r
#
#
# def find_set(x):
#     if parents[x] == x:
#         return x
#     parents[x] = find_set(parents[x])
#     return parents[x]
#
#
# def union(x, y):
#     root_x = find_set(x)
#     root_y = find_set(y)
#
#     if root_x == root_y:
#         return
#     if ranks[root_x] > ranks[root_y]:
#         parents[root_y] = root_x
#     elif ranks[root_x] < ranks[root_y]:
#         parents[root_x] = root_y
#     else:
#         parents[root_y] = root_x
#         ranks[root_x] += 1
#
#
# T = int(input())
# for tc in range(1, T+1):
#     N, M = map(int, input().split())
#     parents, ranks = make_set(N+1)
#     groups = []
#     for i in range(M):
#         s, e = map(int, input().split())
#         union(s, e)
#     for j in range(1, N+1):
#         if find_set(j) not in groups:
#             groups.append(find_set(j))
#     output = len(groups)
#     print(f"#{tc} {output}")


############미완
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    doubles = 0
    while N < M:
        N *= 2
        doubles += 1
    N -= M
    tens = 0
    if N >= 10:
        while N > 10*(2**tens):
            tens += 1
        N -= 10*(2**tens)
        tens += 1
    minus_one = 0
    if N > 0:

        while N > 2**minus_one:
            minus_one += 1
        N -= 2**minus_one
        minus_one += 1
    plus_one = 0
    print(N)
    if N < 0:
        while -N > 2**plus_one:
            plus_one += 1
        N += 2**(plus_one-1)
        plus_one += 1
    ls = [doubles, tens, minus_one, plus_one]
    output = max(ls)
    print(ls)
    for num in ls:
        if 0 < num < max(ls):
            output += 1
    print(f"#{tc} {output}")