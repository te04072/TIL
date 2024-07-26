# def count_character(word, target):
#     return list(word).count(target)

# def count_character(word, target):
#     count = 0
#     for i in range(len(word)):
#         if word[i] == target:
#             count += 1
#     return count
#
#
# result = count_character("Hello, World!", "o")
# print(result)  # 2
#

# def find_min_max(num_list):
#     max_n, min_n = 0, 0
#     for i in range(len(num_list)):
#         if i == 0:
#             min_n = num_list[i]
#             max_n = num_list[i]
#         elif num_list[i] > max_n:
#             max_n = num_list[i]
#         elif num_list[i] < min_n:
#             min_n = num_list[i]
#     minmax = [min_n, max_n]
#     return tuple(minmax)

# def find_min_max(num_list):
#     minmax = [min(num_list), max(num_list)]
#     return tuple(minmax)
#
# result = find_min_max([3, 1, 7, 2, 5])
# print(result)  # (1, 7)

# N = 9
# data_1 = '123456789'
# arr_1 = []
# for i in range(N):
#     arr_1.append(data_1[i])
# print(arr_1)
#
# M = 15
# data_2 = '1 2 3 4 5 6 7 8 9 10 11 12 13 14 15'
# word_list = data_2.split()
# for j in range(M):
#     if int(word_list[j]) % 2 == 1:
#         print(word_list[j])
#
#
# data_1 = 'qweqwYadnOyjnsaU4trwg asjnaAn245krRmkfE 42grTasdnHasdnvEasdn asdevadnBasdanEsdkqefqefvaSasdqaeeqqvedwt5hfbsdT24tewfd'
# '''
# 예시코드
# arr = [1, 2, 3, 4, 5]
# for num in arr:
#     print(num, end='')
# 출력결과 : 12345
# '''
# word = []
#
# for i in range(len(data_1)):
#     if data_1[i] == ' ' or data_1[i].isupper() is True:
#         word.append(data_1[i])
# print(''.join(word))
#
#
#
# data_2 = '걉파반샤팝다푸거맥파바자들퍼바배들밥샵파누타히매니배사바파힘다브사부힙헤베내테치대내'
# arr = []
# arr.extend(data_2.find(x) for x in list('내힘들다'))    # PYTHONIC
# print(arr)
# arr.sort()
# print(arr)
# new_arr = []
# new_arr.extend(data_2[arr[y]] for y in range(4))
# print(''.join(new_arr))

# def restructure_word(word, arr):
#     for i in range(len(word)):
#         if word[i].isdecimal():
#             for j in range(int(word[i])):
#                 arr.pop()
#         else:
#             arr.remove(word[i])
#     return arr
#
# original_word = '코딩 공부는ㄴ 1일ㄹ 1커ㅓ밋ㅅ @@@#^()#_+!&~:"'
# word = '1ㄴ2ㄹ3ㅓ4ㅅ5'
# arr = []
# arr.extend(list(original_word))
# print(arr)
# result = restructure_word(word, arr)
# print(result)
# print(''.join(result))
#

# def reverse_string(word):
#     new_word = []
#     for i in range(1, len(word)+1):
#         new_word.append(word[-i])
#     return ''.join(new_word)
#
# def reverse_string(word):
#     return ''.join(reversed(word))
#
# result = reverse_string("Hello, World!")
# print(result)  # !dlroW ,olleH

# 아래 함수를 수정하시오.
# def remove_duplicates(lst):
#     new_lst = list(set(lst))
#     return new_lst
#

# def remove_duplicates(lst):
#     new_lst = []
#     for i in range(len(lst)):
#         if (lst[i] in lst[i+1:]) is not True:
#             new_lst.append(lst[i])
#     return new_lst
#
# result = remove_duplicates([1, 2, 2, 3, 4, 4, 5])
# print(result)
#

# def remove_duplicates(lst):
#     new_lst = []
#     i = 0
#     while i < len(lst):
#         if (lst[i] in lst[i+1:]) is True:
#             lst.remove(lst[i])
#             i += 1
#         else:
#             i += 1
#     return lst
# result = remove_duplicates([1, 2, 2, 3, 4, 4, 5])
# print(result)

# 아래 함수를 수정하시오.
# def sort_tuple(tpl):
#     lst = list(tpl)
#     lst.sort()
#     new_tuple = tuple(lst)
#     return new_tuple
#
# def sort_tuple(tpl):
#     lst = list(tpl)
#     for i in range(len(lst)):
#         for j in range(0, len(lst)-i-1):
#             if lst[j] > lst[j+1]:
#                 lst[j], lst[j+1] = lst[j+1], lst[j]
#     new_tuple = tuple(lst)
#     return new_tuple
#
# result = sort_tuple((5, 2, 8, 1, 3))
# print(result)

# 아래 함수를 수정하시오.
# def capitalize_words(string):
#    # return string.title()
#     spl_str = string.split()
#     for i in range(len(spl_str)):
#         # spl_str[i] = spl_str[i].capitalize()
#         spl_str[i] = spl_str[i].replace(spl_str[i][0], spl_str[i][0].upper())
#     return ' '.join(spl_str)
#
#
# result = capitalize_words("hello, world!")
# print(result)

# 아래 함수를 수정하시오.
# def even_elements(lst):
#     i = 0
#     while i < len(lst):
#         if lst[i] % 2 == 1:
#             lst.pop(i)
#             i += 1
#         else:
#             i += 1
#     return lst

# def even_elements(lst):
#     new_lst = []
#     new_lst.extend(lst)
#     i = 0
#     while i is not len(new_lst):
#         if new_lst[i] % 2 == 1:
#             new_lst.pop(i)                 # i+=1 넣으면 오답 나옴
#         else:
#             i += 1
#     return new_lst
#
def even_elements(lst):
    new_lst = []
    new_lst.extend(lst)
    for i in range(len(lst)-1, -1, -1):    # 끝에서부터 역으로 진행하여 pop을 해도 index error 발생하지 않음
        if new_lst[i] % 2 == 1:
            new_lst.pop(i)
    return new_lst


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = even_elements(my_list)
print(result)

