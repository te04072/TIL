# for test_case in range(1, 11):
#     T = int(input())
#     buildings = list(map(int, input().split()))
#     ans = 0
#     for i in range(2, T-2):
#         sample = buildings[i-2:i+3]
#         for j in range(5):                      # bubble sort sample
#             for k in range(0, 4-j):
#                 if sample[k] > sample[k+1]:
#                     sample[k], sample[k+1] = sample[k+1], sample[k]
#         if buildings[i] == sample[4]:
#             ans += sample[4] - sample[3]
#     print(f'#{test_case} {ans}')
#

# T = int(input())
# for test_case in range(1, T+1):
#     num = int(input())
#     num_list = list(map(int, input().split()))
#     for i in range(num):
#         for j in range(num - i - 1):
#             if num_list[j] > num_list[j+1]:
#                 num_list[j], num_list[j+1] = num_list[j+1], num_list[j]
#     ans = num_list[num-1] - num_list[0]
#     print(f'#{test_case} {ans}')


# T = int(input())
# for test_case in range(1, T+1):
#     N, M = map(int, input().split())
#     num_list = list(map(int, input().split()))
#     max_sum = 0
#     min_sum = 0
#     for i in range(0, N-M+1):
#         temp = 0
#         for j in range(M):
#             temp += num_list[i+j]
#         if i == 0:
#             max_sum = temp
#             min_sum = temp
#         elif max_sum < temp:
#             max_sum = temp
#         elif min_sum > temp:
#             min_sum = temp
#     ans = max_sum - min_sum
#     print(f'#{test_case} {ans}')

T = int(input())
for test_case in range(1, T+1):
    length = int(input())
    boxes = list(map(int, input().split()))
    ans = 0
    for i in range(length):
        temp = 0
        larger = 0
        for j in range(i+1, length):
            if boxes[i] <= boxes[j]:
                larger += 1
        temp = length - larger - i - 1
        if ans < temp:
            ans = temp
    print(f'#{test_case} {ans}')





