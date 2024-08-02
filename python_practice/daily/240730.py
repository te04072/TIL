# # counting sort
# arr = [1, 3, 8, 3, 4, 5, 2, 0]

# K = 8
# count = [0] * (K+1)
# temp = [0] * len(arr)
# for i in range(len(arr)):
#     count[arr[i]] += 1
# print(count)
# for i in range(1, K+1):
#     count[i] += count[i-1]
# print(count)
# for i in range(len(temp) - 1, -1, -1):
#     count[arr[i]] -= 1
#     temp[count[arr[i]]] = arr[i]
# print(temp)


# T = int(input())
# for test_case in range(1, T+1):
#     N = int(input())
#     num = str(input())
#     array = [int(num[i]) for i in range(N)]
#     count = [0]*10
#     ans = 0
#     index = 0
#     for i in range(len(array)):
#         count[array[i]] += 1
#     for j in range(10):
#         if ans <= count[j]:
#             ans = count[j]
#             index = j
#     print(f'#{test_case} {index} {ans}')


# for test_case in range(1, 11):
#     T = int(input())
#     targets = list(map(int, input().split()))
#     maxI = 0; minI = 0
#     for times in range(1, T+1):      # T회 반복
#         for i in range(100):
#             if targets[maxI] < targets[i]:
#                 maxI = i
#             if targets[minI] > targets[i]:
#                 minI = i
#         targets[maxI] -= 1     # min max에 대해 flatten
#         targets[minI] += 1
#     for i in range(100):
#         if targets[maxI] < targets[i]:
#             maxI = i
#         if targets[minI] > targets[i]:
#             minI = i            # 마지막 대소확인
#     ans = targets[maxI] - targets[minI]
#     print(f'#{test_case} {ans}')

# def run_check(index, list):                       # 판단기준 정확히 세울 것
#     if (((list[index] + 1) in list and (list[index] + 2) in list)
#         or ((list[index] + 1) in list and (list[index] - 1) in list)
#         or ((list[index] -1) in list and (list[index] - 2) in list)) is True:
#         return True
#     else: return False


# def triplet_check(index, list):
#     tri_count = 0                                         # 초기화 시점 주의
#     for card in list:
#         if card == list[index]:
#             tri_count += 1
#     if tri_count >= 3:
#         return True
#     else: return False

# T = int(input())              
# for test_case in range(1, T+1):
#     num = str(input())
#     card_list = [int(num[i]) for i in range(6)]
#     for i in range(6):                                        # babygin 판단 정확히
#         if (run_check(i, card_list) or triplet_check(i, card_list)) is True:
#             baby_gin = 1
#         else:
#             baby_gin = 0
#             break
#     print(f'#{test_case} {baby_gin}')

# K : 한번 충전으로 이동 가능한 거리
# M : 충전 가능 정류장 수
# N : 목표 종점
# 출발점에서 k만큼 이동 가능


T = int(input())
for test_case in range(1, T+1):
    K, N, M = map(int, input().split())
    station_list = [0]*(N+K)
    charge_list = list(map(int, input().split()))
    for i in range(M):
        station_list[charge_list[i]] = 1
    charge_count = 0
    status = 0
    while status < (N - K):
        if (1 in station_list[status+1:status+K+1]) is False:
            charge_count = 0
            break
        else:
            for x in range(status+K, status, -1):
                if station_list[x] == 1:
                    charge_count +=1
                    status = x
                    break
    print(f'#{test_case} {charge_count}')
