# # 아래 함수를 수정하시오.
# def remove_duplicates_to_set(target):
#     return set(target)
#
#
# result = remove_duplicates_to_set([1, 2, 2, 3, 4, 4, 5])
# print(result)

# 아래 함수를 수정하시오.
# def add_item_to_dict(dictionary, key, value):
#     new_dict = dictionary.copy()
#     new = {key: value}
#     new_dict.update(new)
#     return new_dict
#
#
# my_dict = {'name': 'Alice', 'age': 25}
# result = add_item_to_dict(my_dict, 'country', 'USA')
# print(result)

# my_set = {'가', '나', (0, 0)}
# my_dict = {
#         '가': 1,
#         (0, 0): '튜플도 키값으로 사용가능'
#     }
# for key in my_set:
#     print(my_dict.get(key))
# var = (1, 2, 3, 'A')
# my_dict[var] = '변수로도 키 설정 가능'
# print(my_dict)
# # 아래에 코드를 작성하시오.

# data = {
#     '이름': '키위',
#     '종류': '새',
#     '원산지': '호주'
# }
#
# plus_data = {
#     '종류': '과일',
#     '가격': 30000
# }
# print(data.items())
# print(data.values())
# print(data.get('without','unknown'))
# data.update(plus_data)
# print(data)

# data = [
#     {
#         'name': 'galaxy flip',
#         'company': 'samsung',
#         'is_collapsible': True,
#     },
#     {
#         'name': 'ipad',
#         'is_collapsible': False
#     },
#     {
#         'name': 'galaxy fold',
#         'company': 'samsung',
#         'is_collapsible': True
#     },
#     {
#         'name': 'galaxy note',
#         'company': 'samsung',
#         'is_collapsible': False
#     },
#     {
#         'name': 'optimus',
#         'is_collapsible': False
#     },
# ]
#
# key_list = ['name', 'company', 'is_collapsible']
#
# # 아래에 코드를 작성하시오.
# for i in range(len(data)):
#     for key in key_list:
#         if key in data[i].keys():
#             print(f'{key}은/는 {data[i].get(key)}입니다.')
#         else:
#             data[i].setdefault(key, 'unknown')
#             print(f'{key}은/는 {data[i].get(key)}입니다.')
#     print("")

# 아래 함수를 수정하시오.
# def union_sets(A, B):
#     A.update(B)
#     return A
#
#
# result = union_sets({1, 2, 3}, {3, 4, 5})
# print(result)

# 아래 함수를 수정하시오.
# def get_value_from_dict(dict, key):
#     return dict.get(key)
#
#
# my_dict = {'name': 'Alice', 'age': 25}
# result = get_value_from_dict(my_dict, 'name')
# print(result)  # Alice

# def intersection_sets(a, b):
#     c = []
#     for x in a:
#         if x in b:
#             c += [x]
#     c = set(c)
#     return c
#     # return A.intersection(B)
#
#
# result = intersection_sets({1, 2, 3}, {3, 4, 5})
# print(result)

# def get_keys_from_dict(dict):
#     return [x for x in dict.keys()]
#
#
# my_dict = {'name': 'Alice', 'age': 25}
# result = get_keys_from_dict(my_dict)
# print(result)  # ['name', 'age']

def difference_sets(a, b):
    c = []
    for x in a:
        if (x in b) is False:
            c += [x]
    c = set(c)
    return c

    # c = set(a)
    # for x in b:
    #     if x in c:
    #         c.discard(x)
    # return c

    # return a.difference(b) # return a-b


result = difference_sets({1, 2, 3, 4}, {3, 4, 5})
print(result)
