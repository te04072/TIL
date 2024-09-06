# def subsets(x):
#     global cnt
#     temp = 0
#     for i in range(N):
#         if x & 0x1:
#             temp += num_list[i]
#         x >>= 1
#     if temp == K:
#         cnt += 1
#
#
# T = int(input())
# for tc in range(1, T+1):
#     N, K = map(int, input().split())
#     num_list = list(map(int, input().split()))
#     cnt = 0
#     for x in range(0, 1 << N):
#         subsets(x)
#     print(f"#{tc} {cnt}")


# def subsets(x):
#     global min_sum
#     temp = 0
#     for i in range(N):
#         if x & 0x1:
#             temp += num_list[i]
#         x >>= 1
#         if B <= temp < min_sum:
#             min_sum = temp
#
#
# T = int(input())
# for tc in range(1, T+1):
#     N, B = map(int, input().split())
#     num_list = list(map(int, input().split()))
#     min_sum = sum(num_list)
#     for x in range(0, 1 << N):
#         subsets(x)
#     output = min_sum - B
#     print(f"#{tc} {output}")


# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     target = [list(map(int, input().split())) for __ in range(N)]
#     delta = [[1, -1], [1, 1], [-1, 1], [-1, -1]]
#     for i in range(N):
#         for j in range(N):
#             stack = []
#             num_list = []
#             stack.append([i, j])
#             num_list.append(target[i][j])
#             for idx in range(4):
#                 next_i = i + delta[idx][0]
#                 next_j = j + delta[idx][1]
#                 while 0 <= next_i < N and 0 <= next_j < N:
#                     if target[next_i][next_j] not in num_list:
#                         stack.append([next_i, next_j])
#                         num_list.append(target[next_i][next_j])
#                         next_i += delta[idx][0]
#                         next_j += delta[idx][1]
#                     else:
#