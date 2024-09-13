# # 1
# N, M = map(int, input().split())
# M_ssafy = []
# status = False
# for i in range(N):
#     ipt = input()
#     if ipt not in M_ssafy:
#         M_ssafy.append(ipt)
# for j in range(M):
#     ipt = input()
#     if ipt in M_ssafy:
#         print(ipt)
#         status = True
# if not status:
#     print("NO!!")


# 2
# N = int(input())
# problems = [[] for __ in range(11)]
# for _ in range(N):
#     p, g = input().split()
#     problems[int(g)].append(p)
# for i in range(1, 11):
#     if len(problems[i]) > 1:
#         problems[i].sort()
#         for j in problems[i]:
#             print(j)
#     elif problems[i]:
#         print(*problems[i])


# 3
# def solve(problem, index):
#     while problem[2] and problems[index]:
#         problem[2] = int(problem[2]) - 1
#         problems[index] -= 1
#         if problem[0] == 'ko' and int(problem[1]) >= 3:
#             solved[index] += 1
#
#
# N = int(input())
# problems = list(map(int, input().split()))
# M = int(input())
# idx = 0
# left = []
# solved = [0]*N
# while idx < N:
#     if not left or left[2] == 0:
#         left = list(input().split())
#     solve(left, idx)
#     if problems[idx] == 0:
#         idx += 1
# print(*solved)

#4
for tc in range(3):
    N = int(input())
    