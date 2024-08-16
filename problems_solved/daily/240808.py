# for test_case in range(1, 11):
#     T = int(input())
#     calc_0 = list(str(input()))
#     calc_stack = []
#     new_calc = ''
#     output = 0
#     for i in range(len(calc_0)):
#         if calc_0[i] == '+':
#             calc_stack.append(calc_0[i])
#         else:
#             new_calc += calc_0[i]
#             if calc_stack:
#                 new_calc += calc_stack.pop()
#     # print(new_calc)           # 후위표기식
#     for i in range(len(new_calc)):
#         temp = 0
#         if new_calc[i] == '+':
#             temp += calc_stack.pop()
#             temp += calc_stack.pop()
#             calc_stack.append(temp)
#         else:
#             calc_stack.append(int(new_calc[i]))
#     output = calc_stack.pop()
#     print(f"#{test_case} {output}")


# T = int(input())                          # 숫자 2개 미만에 연산자 / 연산자 오기 전에 끝나면 error
# for test_case in range(1, T+1):
#     calc = list(input().split())
#     operator = ['+', '-', '*', '/']
#     calc_stack = []
#     output = 0
#     for i in range(len(calc)):
#         temp = 0
#         if calc[i] == '.':
#             if len(calc_stack) == 1:
#                 output += calc_stack.pop()
#             else:
#                 output = 'error'
#             break
#         elif (calc[i] in operator) is False:
#             calc_stack.append(int(calc[i]))
#         elif calc[i] in operator:
#             if len(calc_stack) > 1:
#                 if calc[i] == '+':
#                     temp += calc_stack.pop()
#                     temp += calc_stack.pop()
#                     calc_stack.append(temp)
#                 elif calc[i] == '-':
#                     temp -= calc_stack.pop()
#                     temp += calc_stack.pop()
#                     calc_stack.append(temp)
#                 elif calc[i] == '*':
#                     temp += calc_stack.pop()
#                     temp *= calc_stack.pop()
#                     calc_stack.append(temp)
#                 elif calc[i] == '/':
#                     divisor = calc_stack.pop()
#                     temp += calc_stack.pop()
#                     temp //= divisor
#                     calc_stack.append(temp)
#             else:
#                 output = 'error'
#                 break
#     print(f"#{test_case} {output}")

def no_way_home(i, j):
    way = True                                  # 주변을 탐색하여 벽이 아닌 곳이 있으면 True
    for x in range(4):
        if (0 <= (i + delta_i[x]) < N) and (0 <= (j + delta_j[x]) < N):
            if target[i + delta_i[x]][j + delta_j[x]] != 1:
                break
    else:
        way = False
    return way


# 백트래킹
T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    target = [list(map(int, input())) for __ in range(N)]
    delta_i = [0, -1, 0, 1]
    delta_j = [1, 0, -1, 0]
    start_i, start_j = 0, 0
    for i in range(N):          # 출발점 찾기
        for j in range(N):
            if target[i][j] == 2:
                start_i, start_j = i, j
                break
    cur_i, cur_j = start_i, start_j
    ans = -1
    stack = []
    while target[cur_i][cur_j] != 3:
        for k in range(4):                      # 상하좌우에서 출구 탐색
            if (0 <= (cur_i + delta_i[k]) < N) and (0 <= (cur_j + delta_j[k]) < N):
                if target[cur_i + delta_i[k]][cur_j + delta_j[k]] == 3:
                    ans = 1
                    break
        else:                                   # 주변에 출구가 없다면
            for t in range(4):
                if (0 <= (cur_i + delta_i[t]) < N) and (0 <= (cur_j + delta_j[t]) < N):
                    if target[cur_i + delta_i[t]][cur_j + delta_j[t]] != 1:         # target[][] == 0 (x)
                        cur_i += delta_i[t]
                        cur_j += delta_j[t]
                        target[cur_i][cur_j] = 1
                        stack.append([cur_i, cur_j])             # 값이 0인 좌표를 1로 바꾸고 스택에 추가하며 이동
                        break
                    if no_way_home(cur_i, cur_j) is False:       # 길이 막혔다면 길이 나올때까지 백트래킹
                        while no_way_home(cur_i, cur_j) is False:
                            backtrack = stack.pop()
                            cur_i, cur_j = backtrack[0], backtrack[1]
                            if not stack and no_way_home(cur_i, cur_j) is False:    # 끝까지 백트래킹을 해도 길이 없으면 0
                                ans = 0
                                break
                if ans == 0:
                    break
        if ans == 1 or ans == 0:
            break
    print(f"#{test_case} {ans}")




