def solution(str1, str2):
    dict_1 = {}
    dict_2 = {}
    for i in range(len(str1)-1):
        if str1[i].isalpha() and str1[i+1].isalpha():
            new_str = str1[i]+str1[i+1]
            value = dict_1.get(new_str, 0)
            value += 1
            dict_1.update({new_str: value})
    for i in range(len(str2)-1):
        if str2[i].isalpha() and str2[i+1].isalpha():
            new_str = str2[i]+str2[i+1]
            value = dict_2.get(new_str, 0)
            value += 1
            dict_2.update({new_str: value})
    intersection = 0
    union = 0
    for key in dict_1:
        if key in dict_2:
            intersection += min(dict_1[key], dict_2[key])
            union += max(dict_1[key], dict_2[key])
        else:
            union += dict_1[key]
    for key in dict_2:
        if key not in dict_1:
            union += dict_2[key]
    if union:
        answer = int(65536*intersection/union)
    elif union == intersection == 0:
        answer = 1
    else:
        answer = 0
    return answer


A = input().upper()
B = input().upper()
print(solution(A, B))