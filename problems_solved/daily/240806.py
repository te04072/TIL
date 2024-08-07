# # pascal - for loop
# def pascal_print(num):
#     cnt = 1
#     while cnt <= num:
#         if cnt == 1:
#             print(1)
#             cnt += 1
#         else:
#             temp_line = [1]*cnt
#             for i in range(cnt):
#                 if i != 0 and i != (cnt-1):
#                     temp_line[i] = pascal_line[i-1] + pascal_line[i]
#             cnt += 1
#             pascal_line = temp_line[:]
#             print(*pascal_line)
#
#
# T = int(input())
# for test_case in range(1, T+1):
#     N = int(input())
#     print(f"#{test_case}")
#     pascal_print(N)


# pascal - memoization
# def pascal_tri(num):
#     cnt = 1
#     output = [[1]]
#     while cnt <= num:
#         if cnt == 1:
#             cnt += 1
#             continue
#         else:
#             output += [[1]*cnt]
#             for x in range(1, cnt):
#                 if 0 < x < cnt - 1:
#                     output[cnt-1][x] = output[cnt-2][x-1] + output[cnt-2][x]
#             cnt += 1
#     return output
#
#
# T = int(input())
# N = [0]*T
# max_n = 0
# for i in range(T):
#     N[i] = int(input())
#     if N[i] > max_n:
#         max_n = N[i]
# target = pascal_tri(max_n)
# for test_case in range(1, T+1):
#     print(f"#{test_case}")
#     for j in range(1, N[test_case-1]+1):
#         print(*target[j-1])


# stack
# def push(item, sz):
#     global top
#     top += 1
#     if top == sz:
#         print('overflow')
#     else:
#         stack[top] = item
#
#
# def pop():
#     global top
#     if top == -1:
#         print('underflow')
#         return 0
#     else:
#         top -= 1
#         return stack[top+1]
#
#
# def peek():
#     return stack[top]


# T = int(input())
# for test_case in range(1, T+1):
#     string = input()
#     size = len(string)
#     no_dpl = []
#     temp = None
#     for i in range(size):
#         print(temp, string[i])
#         if no_dpl and no_dpl[-1] == string[i]:    # 스택 내부 글자 = 이번 글자
#             no_dpl.pop()
#         if temp == string[i]:           # 직전 글자 = 이번 글자
#             continue
#         if len(no_dpl) > 1 and no_dpl[-1] == no_dpl[-2]:     # pop했더니 겹치는 경우(겹친다면 한 글자만)
#
#         elif len(no_dpl) == 0 or no_dpl[-1] != string[i]:  # append는 첫 요소거나 top이 중복이 아닐 때
#             no_dpl.append(string[i])
#         temp = string[i]
#         print(no_dpl)


# T = int(input())
# for test_case in range(1, T+1):
#     string = input()
#     size = len(string)
#     # ['(', ')', '{', '}']
#     bracket_dict = {'(': 0,  ')': 1,  '{': 2,  '}': 3}
#     bracket_stack = []
#     ans = 1
#     t = 0
#     for i in range(size):
#         if string[i] in bracket_dict.keys():
#             bracket_stack.append(string[i])
#     while len(bracket_stack) > 0:
#         if len(bracket_stack) == 1:         # 쌍을 못 맞추고 1개만 남았으면 break
#             ans = 0
#             break
#         cur = bracket_dict[bracket_stack[t-1]]           # 맨 끝과 끝에서 두번째
#         nxt = bracket_dict[bracket_stack[t-2]]
#         if len(bracket_stack) == 2:
#             if cur//2 == nxt//2 and cur != nxt:
#                 break
#         if cur % 2 == 0:                   # top이 닫는 괄호가 아니면 break
#             ans = 0
#             break
#         if nxt % 2 == 0 and cur//2 != nxt//2:                        # 맨 끝이 닫는 괄호이고 그 다음이 여는 괄호라면 쌍여부
#             ans = 0
#             break
#         elif nxt % 2 == 0 and cur//2 == nxt//2:             # 한 쌍이라면 2개 pop 후 다음루프
#             temp = []
#             for j in range(-t):                             # 쌓인 괄호 t개를 temp에 저장 후 pop
#                 temp.append(bracket_stack.pop())
#             bracket_stack.pop()
#             bracket_stack.pop()
#             bracket_stack += temp[::-1]
#             t = 0
#             continue
#         elif nxt % 2 == 1 and cur % 2 == 1:                  # 마지막 2개가 모두 닫는 괄호라면 다음 요소 체크
#             t -= 1
#     print(f"#{test_case} {ans}")







