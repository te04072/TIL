# T = int(input())                                    # 달팽이 숫자
# for test_case in range(1, T+1):
#     N = int(input())
#     output = [[0]*N for __ in range(N)]             # N*N 2차원 리스트
#     num = 0
#     snail_i = 0
#     snail_j = 0
#     dx = [1, 0, -1, 0]                              # delta
#     dy = [0, 1, 0, -1]
#     t = 0
#     while num < N**2:
#         num += 1                                    # 루프가 시작되면 지정된 좌표에 숫자 입력
#         output[snail_i][snail_j] = num
#         snail_i += dy[t]                            # delta 값에 따라 좌표 이동
#         snail_j += dx[t]
#         if ((0 <= snail_i < N) is False or (0 <= snail_j < N) is False) or output[snail_i][snail_j] != 0:
#             snail_i -= dy[t]                        # 이동한 좌표가 인덱스를 벗어나거나 이미 입력된 값이 있는 경우
#             snail_j -= dx[t]                        # 좌표를 되돌린 후 다음 delta 로 넘어가 방향전환
#             t = (t + 1) % 4
#             snail_i += dy[t]
#             snail_j += dx[t]
#     print(f'#{test_case}')
#     for i in range(N):
#         print(*output[i])

# def prime_factor(number, div):
#     count = 0
#     while number % div == 0:
#         number /= div
#         count += 1
#     return count
#
#
# T = int(input())
# for test_case in range(1, T+1):
#     num = int(input())
#     primes = [2, 3, 5, 7, 11]
#     output = [0] * len(primes)
#     for i in range(len(primes)):
#         output[i] = prime_factor(num, primes[i])
#     print(f'#{test_case}', end=" ")
#     print(*output)


# T = int(input())
# for test_case in range(1, T+1):
#     N = int(input())
#     number = list(map(int, input()))
#     output = 0
#     temp = 0
#     for i in range(N):
#         if number[i] == 1:
#             temp += 1
#         else:
#             if output < temp:
#                 output = temp
#             temp = 0
#         if i == N-1:
#             if output < temp:
#                 output = temp
#     print(f'#{test_case} {output}')

# T = int(input())
# for test_case in range(1, T+1):
#     N = int(input())
#     stations = [[0]*2 for __ in range(N)]
#     for i in range(N):
#         stations[i] = list(map(int, input().split()))
#     P = int(input())
#     output = [0]*P
#     for p in range(P):
#         temp = int(input())
#         count = 0
#         for j in range(N):
#             if stations[j][0] <= temp <= stations[j][1]:
#                 count += 1
#         output[p] = count
#     print(f'#{test_case}', end=" ")
#     print(*output)


# def bubble_sort(ls):
#     length = len(ls)
#     for i in range(length):
#         for j in range(length-i-1):
#             if ls[j] > ls[j+1]:
#                 ls[j], ls[j+1] = ls[j+1], ls[j]
#     return ls
#
#
# def selection_sort(ls):
#     length = len(ls)
#     for i in range(length-1):
#         min_i = i
#         for j in range(i+1, length):
#             if ls[min_i] > ls[j]:
#                 min_i = j
#         ls[min_i], ls[i] = ls[i], ls[min_i]
#     return ls
#
#
# T = int(input())
# for test_case in range(1, T+1):
#     N = int(input())
#     target = list(map(int, input().split()))
#     # bubble_sort(target)
#     selection_sort(target)
#     print(f'#{test_case}', end=" ")
#     print(*target)
#
# T = int(input())
# for test_case in range(1, T+1):
#     N = int(input())
#     target = list(map(int, input().split()))
#     for i in range(N-1):
#         max_i = i
#         min_i = i
#         for j in range(i+1, N):
#             if target[j] > target[max_i]:
#                 max_i = j
#             if target[j] < target[min_i]:
#                 min_i = j
#         if i % 2 == 0:
#             target[i], target[max_i] = target[max_i], target[i]
#         else:
#             target[i], target[min_i] = target[min_i], target[i]
#     target = target[:10]                        # 문제조건 주의
#     print(f'#{test_case}', end=" ")
#     print(*target)

# def binary_search_count(N, key):
#     start = 1
#     end = N
#     cnt = 0
#     while start <= end:
#         middle = int((start+end)/2)
#         cnt += 1
#         if middle == key:
#             return cnt
#         elif middle > key:
#             end = middle
#         else: start = middle
#
#
# T = int(input())
# for test_case in range(1, T+1):
#     P, Pa, Pb = map(int, input().split())
#     a_count = binary_search_count(P, Pa)
#     b_count = binary_search_count(P, Pb)
#     ans = None
#     if a_count > b_count:
#         ans = 'B'
#     elif a_count == b_count:
#         ans = '0'
#     else: ans = "A"
#     print(f'#{test_case} {ans}')


#######LADDER######

def direc_check(ls, pos):
    if pos == 0:
        if ls[pos+1] == 1:
            return 'right'
    elif pos == len(ls) - 1:
        if ls[pos-1] == 1:
            return 'left'
    elif ls[pos + 1] == 1:
        return 'right'
    elif ls[pos - 1] == 1:
        return 'left'
    else:
        return 'go'


def move_check(ls, pos, direc):
    while (0 <= pos+direc <= 99) and ls[pos+direc] == 1:
        pos += direc
    return pos

    # while (0 <= pos+direc <= 99) and ls[pos+direc] == 1:       #이 코드는 왜 진동하는가
    #     pos += direc
    #     if pos == 0 or 99:
    #         break


for test_case in range(1, 11):
    T = int(input())
    target = [list(map(int, input().split())) for __ in range(100)]
    start_j = 0
    ans_j = 0
    for x in range(100):
        if target[99][x] == 2:
            start_j = x

    cur = start_j
    for m in range(98, -1, -1):
        print(cur)
        if direc_check(target[m], cur) == 'right':
            cur = move_check(target[m], cur, 1)
        elif direc_check(target[m], cur) == 'left':
            cur = move_check(target[m], cur, -1)
        else:
            continue
    ans_j = cur
    print(f'#{test_case} {ans_j}')