# for test_case in range(1, 11):
#     N = int(input())
#     string = str(input())
#     new_string = ''
#     calc_stack = []
#     for i in range(N):
#         if string[i] == '*':                            # 우선도 높은 *
#             calc_stack.append(string[i])
#
#         elif string[i] == '+':                          # 우선도 낮은 +
#             while calc_stack:
#                 new_string += calc_stack.pop()
#             calc_stack.append(string[i])    # 스택의 *를 모두 pop한 후 string에 추가, +를 push
#         else:                                           # 피연산자
#             new_string += string[i]
#     while calc_stack:
#         new_string += calc_stack.pop()
#     # print(new_string)
#     for i in range(N):
#         if calc_stack and new_string[i] == '*':
#             temp = int(calc_stack.pop())
#             temp *= int(calc_stack.pop())
#             calc_stack.append(temp)
#         elif calc_stack and new_string[i] == '+':
#             temp = int(calc_stack.pop())
#             temp += int(calc_stack.pop())
#             calc_stack.append(temp)
#         else:
#             calc_stack.append(new_string[i])
#     output = calc_stack.pop()
#     print(f"#{test_case} {output}")


# T = int(input())
# for test_case in range(1, T+1):
#     size = int(input())
#     target = [list(map(int, input().split())) for __ in range(size)]
#     output = 0
#     for i in range(size):
#         for j in range(size):
#

def tournament(ls1, ls2):
    if len(ls1) == 1:
        if ls1[0] != 1:
            if ls1[0] >= ls2[0]:
                ls = ls1
            else:
                ls = ls2
        else:
            if ls2[0] == 2:
                ls = ls2
            else:
                ls = ls1
        return ls
    else:
        return ls[:1+len(ls)//2], ls[1+len(ls)//2:]


T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    students = list(map(int, input().split()))
    for i in range(N):
        students[i] = [students[i], i+1]
    print(students)

    print(tournament(students))


