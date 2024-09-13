# # T = int(input())
# # for tc in range(1, T+1):
# #     n, k = map(int, input().split())
# #     planets = sorted(list(map(int, input().split())))
# #     output = 0
# #     target = sum(planets)
# #     while target > k:
# #         for i in range(n-1, -1, -1):
# #             if 0 < planets[i] <= k:                 # 함선 수로 점령 가능한 가장 큰 행성 점령
# #                 k += planets[i]
# #                 target -= planets[i]
# #                 planets[i] = 0
# #                 output += 1
# #                 break
# #         else:
# #             output = -1
# #             break
# #     print(f"#{tc} {output}")
#
#########################################
# from collections import deque
#
#
# T = int(input())
# for tc in range(1, T+1):
#     n, k = map(int,input().split())
#     planets = sorted(list(map(int,input().split())))
#     tries = 0
#     dq = deque()
#     i = 0
#
#     while i < n:
#         if k >= planets[i]:
#             dq.append(planets[i])
#             i += 1
#         elif dq:
#             k += dq.pop()
#             tries += 1
#         else:
#             tries = -1
#             break
#     while dq:
#         if dq[-1] <= k:
#             last = dq.pop()
#             k -= last
#         else:
#             k += last*2
#             tries += 1
#     print(f'#{tc} {tries}')

for tc in range(1, 11):
    n, s = map(int, input().split())
    i_lst = list(map(int, input().split()))
    max_num = max(i_lst)

    # 리스트 구현
    number_lst = [[] for _ in range(max_num + 1)]
    for i in range(0, n, 2):
        number_lst[i_lst[i]].append(i_lst[i + 1])

    visited = [0] * (max_num + 1)
    q = []
    visited[s] = 1
    for num in number_lst[s]:
        q.append(num)
        visited[num] = 1
    level = 0
    result = []
    # print(q)
    if len(q) == 1:
        print(f'#{tc} {q[0]}')
    else:
        while q:
            temp = []
            while q:
                s = q.pop(0)
                for num in number_lst[s]:
                    if not visited[num]:
                        temp.append(num)
                        visited[num] = 1
            q = temp
            result.append(temp[:])
            print(temp)
        print(f'#{tc} {max(result[-2])}')
