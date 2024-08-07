# def is_palindrome(string):
#     ans = True
#     t = 0
#     while t != len(string) // 2:
#         if string[t] == string[-t-1]:
#             t += 1
#         else:
#             ans = False
#             break
#     return ans

# T = int(input())
# for test_case in range(1, T+1):
#     N, M = map(int, input().split())
#     output = None
#     target = [list(map(str, input())) for __ in range(N)]
#     for i in range(N):
#         for j in range(N-M+1):
#             if target[i][j] == target[i][j+M-1]:
#                 sample = target[i][j:j+M]
#                 if is_palindrome(sample) is True:
#                     output = sample
#     if output is None:
#         new_target = [['']*N for ___ in range(N)]
#         for x in range(N):
#             for y in range(N):
#                 if x > y:
#                     target[x][y], target[y][x] = target[y][x], target[x][y]
#         for i in range(N):
#             for j in range(N-M+1):
#                 if target[i][j] == target[i][j+M-1]:
#                     sample = target[i][j:j+M]
#                     if is_palindrome(sample) is True:
#                         output = sample
#     output = ''.join(output)
#     print(f"#{test_case} {output}")


# for test_case in range(1, 11):
#     tc = int(input())
#     target = [list(map(str, input())) for __ in range(100)]
#     output = 0
#     size = 0
#     for i in range(100):
#         for j in range(99):
#             for k in range(99, j, -1):
#                 if target[i][j] == target[i][k]:
#                     sample = target[i][j:k+1]
#                     if is_palindrome(sample) is True:
#                         size = k-j+1
#                         if output < size:
#                             output = size
#     for x in range(100):
#         for y in range(100):
#             if x > y:
#                 target[x][y], target[y][x] = target[y][x], target[x][y]
#     for i in range(100):
#         for j in range(99):
#             for k in range(99, j, -1):
#                 if target[i][j] == target[i][k]:
#                     sample = target[i][j:k+1]
#                     if is_palindrome(sample) is True:
#                         size = k-j+1
#                         if output < size:
#                             output = size
#
#     print(f"#{tc} {output}")


def key_count(target, key):
    len_t = len(target)
    len_k = len(key)
    cnt = 0
    cur = -1
    while cur <= len_t - len_k:
        temp = cur                      # temp 위치를 기준으로 하지 않으면 마지막 일치시점을 기준으로 재검색함
        for x in range(len_k):
            cur += 1
            if target[cur] != key[x]:
                cur = temp + 1
                break
        else:
            cnt += 1
    return cnt


T = int(input())
for test_case in range(1, T+1):
    A, B = input().split()
    hot_key = key_count(A, B)
    output = len(A) - hot_key * (len(B)-1)
    print(f"#{test_case} {output}")
