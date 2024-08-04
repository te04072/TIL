# for test_case in range(1, 11):
#     T = int(input())
#     target = [list(map(int, input().split())) for __ in range(100)]
#     temp = 0
#     ans = 0
#     for i in range(100):
#         for j in range(100):
#            temp += target[i][j]
#         if temp > ans:
#             ans = temp
#         temp = 0

#     for j2 in range(100):
#         for i2 in range(100):
#            temp += target[i2][j2]
#         if temp > ans:
#             ans = temp
#         temp = 0
    
#     for i3 in range(100):
#         temp += target[i3][i3]
#     if temp > ans:
#         ans = temp
    
#     temp = 0
#     for i4 in range(100):
#         temp += target[i4][99 - i4]
#     if temp > ans:
#         ans = temp

#     print(f'#{T} {ans}')

# T = int(input())
# for test_case in range(1, T+1):
#     N = int(input())
#     target = list(map(int, input().split()))
#     for i in range(N):
#         for j in range(len(target) - i - 1):
#             if target[j] > target[j+1]:
#                 target[j], target[j+1] = target[j+1], target[j]
#     print(f'#{test_case} ', end = "")
#     print(*target)

# T = int(input())
# for test_case in range(1, T+1):
#     N = int(input())
#     target = list(map(int, input().split()))
#     for i in range(N):
#         min_i = i
#         for j in range(i+1, N):
#             if target[j] < target[min_i]:
#                 min_i = j
#         target[i], target[min_i] = target[min_i], target[i]
#     print(f'#{test_case} ', end = "")
#     print(*target)

# def no_dupl(list):
#     length = len(list)
#     temp = [0]*length
#     ans = True
#     for i in range(length):
#         if temp[list[i]-1] == 0:
#             temp[list[i]-1] += 1
#         else:
#             ans =  False
#             break
#     return ans
        

# T = int(input())
# for test_case in range(1, T+1):
#     target = [list(map(int, input().split())) for __ in range(9)]
#     ans = 1
#     for row in range(9):
#         if no_dupl(target[row]) is False:
#             ans = 0
#             break

#     for i in range(9):
#         for j in range(9):
#             if i > j:
#                 target[i][j], target[j][i] = target[j][i], target[i][j]
#     for col in range(9):
#         if no_dupl(target[col]) is False:
#             ans = 0
#             break
    
#     for box1 in range(3):
#         for box2 in range(3):
#             sample = []
#             for x in range(3):
#                 sample.extend(target[box1*3+x][box2*3:box2*3+3])
#             if no_dupl(sample) is False:
#                 ans = 0

#     print(f'#{test_case} {ans}')

# def puzzle(list, num):
#     cnt = 0
#     ans = 0
#     cur = 0
#     while cur < len(list):
#         if list[cur] == 1:
            
#             while list[cur] == 1:
#                 cnt += 1
#                 cur += 1
#                 if cur == len(list):
#                     break
#             if cnt == num:
#                 ans += 1
#                 cnt = 0
#             else: cnt = 0
#         else:
#             cur += 1
#     return ans

# T = int(input())
# for test_case in range(1, T+1):
#     N, K = map(int, input().split())
#     target = [list(map(int, input().split())) for __ in range(N)]
#     answer = 0
#     for i in range(N):
#         answer += puzzle(target[i], K)

#     for m in range(N):
#         for n in range(N):
#             if m > n:
#                 target[m][n], target[n][m] = target[n][m], target[m][n]
#     for j in range(N):
#         answer += puzzle(target[j], K)

#     print(f'#{test_case} {answer}')


# def is_in(elem, list):
#     ans = False
#     for i in range(len(list)):
#         if list[i] == elem:
#             ans = True
#             break
#     return ans
            

# T = int(input())
# for test_case in range(1, T+1):
#     N = int(input())
#     red_list = []
#     blue_list = []
#     ans = 0
#     for __ in range(N):
#         temp = list(map(int, input().split()))
#         if temp[4] == 1:
#             for i in range(temp[0],temp[2]+1):
#                 for j in range(temp[1], (temp[3]+1)):
#                     red_list+((i, j))
#         if temp[4] == 2:
#             for i in range(temp[0],temp[2]+1):
#                 for j in range(temp[1], (temp[3]+1)):
#                     blue_list.append((i, j))
#     for item in red_list:
#         if is_in(item, blue_list) is True:
#             ans += 1
#     print(f'#{test_case} {ans}')

# def killer(list, M, row, col):
#     sum = 0
#     for i in range(row, row+M):
#         for j in range(col, col+M):
#             sum += list[i][j]
#     return sum

# T = int(input())
# for test_case in range(1, T+1):
#     N, M = map(int, input().split())
#     target = [list(map(int, input().split())) for __ in range(N)]
#     ans = 0
#     temp = 0
#     for i in range(0, N-M+1):
#         for j in range(0, N-M+1):
#             temp = killer(target, M, i, j)
#             if ans < temp:
#                 ans = temp
#     print(f'#{test_case} {ans}')


# def subsets(A):                     # 부분집합의 합을 공집합을 포함한 재귀함수로 구현
#     if len(A) == 1:
#         return [0, A[0]]
#     else:
#         return subsets(A[0:-1]) + [A[-1]+item for item in subsets(A[0:-1])]

# T = int(input())
# for test_case in range(1, T+1):
#     target = list(map(int, input().split()))
#     if 0 in subsets(target)[1:]:            # subsets()의 0번 인덱스는 공집합의 합인 0
#         ans = 1
#     else: ans = 0
#     print(f'#{test_case} {ans}')



#### 비트연산자 ####

T = int(input())

arr = [x for x in range(1, 13)]
subsets = []
for i in range(1 << 12):
    temp = []
    for j in range(12):
        if i & (1 << j):
            temp.append(arr[j])
    subsets.append(temp)

for test_case in range(1, T+1):
    ans = 0; temp = 0
    N, K = map(int, input().split())
    for i in range(len(subsets)):
        if len(subsets[i]) == N:
            for j in range(len(subsets[i])):
                temp += subsets[i][j]
            if temp == K:
                ans += 1
#             temp = 0
#     print(f'#{test_case} {ans}')

