# T = int(input())
# for test_case in range(1, T+1):
#     target = str(input())
#     ans = 1
#     for i in range(len(target)//2):
#         if target[i-1] != target[-i]:
#             ans = 0
#     print(f'#{test_case} {ans}')


# T = int(input())
# for test_case in range(1, T+1):
#     target = str(input())
#     length = len(target)
#     output = [0]*length
#     for i in range(length-1, -1, -1):
#         if target[i] == 'p':
#             output[length - i - 1] = 'q'
#         elif target[i] == 'q':
#             output[length - i - 1] = 'p'
#         elif target[i] == 'b':
#             output[length - i - 1] = 'd'
#         elif target[i] == 'd':
#             output[length - i - 1] = 'b'
#     string = ''.join(output)
#     print(f'#{test_case} {string}')


# T = int(input())
# for test_case in range(1, T+1):
#     str1 = str(input())
#     str2 = str(input())
#     output = 0
#     for i in range(len(str1)):
#         cnt = 0
#         for j in range(len(str2)):
#             if str1[i] == str2[j]:
#                 cnt += 1
#         if cnt > output:
#             output = cnt
#     print(f'#{test_case} {output}')


# T = int(input())
# for test_case in range(1, T+1):
#     str1 = str(input())
#     str2 = str(input())
#     ans = 0
#     for i in range(len(str2)-len(str1)):
#         if str2[i] == str1[0]:
#             print(str2[i:i+len(str1)])
#             if str2[i:i+len(str1)] == str1:
#                 ans = 1
#                 break
#     print(f'#{test_case} {ans}')


def list_switch(dict1, dict2, ls):
    for i in range(len(ls)):
        for j in range(len(dict1)):
            if ls[i] == dict1[j]:
                ls[i] = dict2[j]
    return ls


def bubble_sort(ls):
    for i in range(len(ls)):
        for j in range(len(ls)-i-1):
            if ls[j] > ls[j+1]:
                ls[j], ls[j+1] = ls[j+1], ls[j]
    return ls


T = int(input())
alphas = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
numbers = [i for i in range(10)]
my_dict = {alphas[i]: i for i in range(10)}
rev_dict = {value: key for key, value in my_dict.items()}

for test_case in range(1, T+1):
    tc, length = map(str, input().split())
    target = list(map(str, input().split()))
    new_list = ['']*int(length)
    count_list = [0]*10
    for i in range(int(length)):
        for j in range(10):
            if target[i] == alphas[j]:
                count_list[j] += 1
    for m in range(9):
        count_list[m+1] += count_list[m]
    for n in range(10):
        for k in range(count_list[n]):
            if n == 0:
                new_list[0:count_list[n]] = "ZRO"
            else:
                new_list[count_list[n-1]:count_list[n]] = alphas[n]
    print(f'#{test_case}')
    print(new_list)




# 2. dictionary
# for test_case in range(1, T+1):
#     tc, length = map(str, input().split())
#     target = list(map(str, input().split()))
#     for i in range(int(length)):
#         target[i] = my_dict.get(target[i])
#     bubble_sort(target)
#     for j in range(int(length)):
#         target[j] = rev_dict.get(target[j])
#     print(f'#{test_case}')
#     print(*target)

# 1. list
# for test_case in range(1, T+1):
#     tc, length = map(str, input().split())
#     target = list(map(str, input().split()))
#     list_switch(alphas, numbers, target)
#     bubble_sort(target)
#     list_switch(numbers, alphas, target)
#     print(f'#{test_case}')
#     print(*target)


# T = int(input())
# for test_case in range(1, T+1):
#     target = [list(map(str, input())) for __ in range(5)]
#     max_l = 0
#     string = ''
#     for x in range(5):
#         if len(target[x]) > max_l:
#             max_l = len(target[x])
#     for y in range(5):
#         diff = max_l - len(target[y])
#         target[y].extend(['']*diff)
#
#     for j in range(max_l):
#         for i in range(5):
#             string += target[i][j]
#     print(f'#{test_case}', end=' ')
#     print(string)
