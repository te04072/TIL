# T = int(input())
# for test_case in range(1, T+1):
#     N = int(input())
#     target = [list(input()) for __ in range(N)]
#     ans = "NO"
#     for i in range(N):
#         for j in range(0, N):
#             if target[i][j] == 'o':
#                 if 0 <= j < N-4:
#                     if target[i][j:j+5] == ['o']*5:
#                         ans = "YES"
#                         break
#                 if 0 <= i < N - 4:
#                     if [target[i+t][j] for t in range(5)] == ['o']*5:
#                         ans = "YES"
#                         break
#                 if 0 <= i < N-4 and 0 <= j < N-4:
#                     if [target[i+t][j+t] for t in range(5)] == ['o']*5:
#                         ans = "YES"
#                         break
#                 if 0 <= i < N-4 and 4 <= j < N:
#                     if [target[i+t][j-t] for t in range(5)] == ['o']*5:
#                         ans = "YES"
#                         break
#         if ans == "YES":
#             break
#     print(f"#{test_case} {ans}")


# T = int(input())
# for test_case in range(1, T+1):
#     size, times = map(int, input().split())
#     target = [[0]*size for __ in range(size)]
#     target[size // 2 - 1][size // 2 - 1] = 2
#     target[size // 2][size // 2] = 2
#     target[size // 2][size // 2 - 1] = 1
#     target[size // 2 - 1][size // 2] = 1
#     delta = [[1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0], [-1, -1], [0, -1], [1, -1]]      # 하, 우하, 우, 우상, 상, 좌상, 좌, 좌하
#     for t in range(times):
#         x, y, color = map(int, input().split())
#         i = y-1
#         j = x-1
#         target[i][j] = color
#         for d in range(8):
#             adj_i = i + delta[d][0]
#             adj_j = j + delta[d][1]
#             if (0 <= adj_i < size) and (0 <= adj_j < size):                           # 인덱스 범위 이내에서
#                 if target[adj_i][adj_j] * target[i][j] == 2:                       # 0도 아니고 같은 수도 아닐 때
#                     k = 1
#                     change = True
#                     while target[i+delta[d][0]*k][j+delta[d][1]*k] != color:        # 같은 색깔의 돌을 만날 때까지
#                         k += 1
#                         if not ((0 <= i+delta[d][0] * k < size) and (0 <= j + delta[d][1] * k < size)):
#                             k -= 1
#                             change = False
#                             break
#                         if target[i+delta[d][0]*k][j+delta[d][1]*k] == 0:
#                             change = False
#                             break
#                     if change:
#                         for p in range(1, k):
#                             target[i + delta[d][0] * p][j + delta[d][1] * p] = color
#     black = 0
#     white = 0
#     for i in range(size):                                                           # 정산. sum 으로도 접근 가능. 0까지 세지 않도록 주의
#         for j in range(size):
#             if target[i][j] == 1:
#                 black += 1
#             elif target[i][j] == 2:
#                 white += 1
#     print(f"#{test_case} {black} {white}")


T = int(input())
for test_case in range(1, T+1):
    string = input()
    cnt = 0
    output = 0
    for i in range(len(string)-1):
        if string[i] == '(':
            if string[i+1] == '(':
                cnt += 1
                output += 1
        else:
            if string[i-1] == '(':
                output += cnt
            else:
                cnt -= 1
    print(f"#{test_case} {output}")
