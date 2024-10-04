def solution(str1, str2):
    dict_1 = {}
    dict_2 = {}
    # str1과 str2에서 나온 글자쌍의 횟수를 dictionary 에 저장
    for i in range(len(str1)-1):
        if str1[i].isalpha() and str1[i+1].isalpha():
            new_str = str1[i]+str1[i+1]
            value = dict_1.get(new_str, 0)      # 글자쌍의 등장횟수를 value에 저장, 없던 글자쌍이면 0 저장
            value += 1
            dict_1.update({new_str: value})     # value+1을 해당 글자쌍에 부여
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
            intersection += min(dict_1[key], dict_2[key])   # 양쪽에 모두 존재하는 글자쌍이라면 적은 쪽의 횟수를 교집합 길이에 합산
            union += max(dict_1[key], dict_2[key])          # 많은 쪽의 횟수를 합집합 길이에 합산
        else:
            union += dict_1[key]                            # dict_1에만 존재하는 글자쌍 등장 횟수를 합집합 길이에 합산
    for key in dict_2:
        if key not in dict_1:
            union += dict_2[key]                            # dict_2에만 존재하는 글자쌍 등장 횟수를 합집합 길이에 합산
    if union:
        answer = int(65536*intersection/union)              # 유사도 연산 후 65536 곱하기
    elif union == intersection == 0:
        answer = 65536
    else:
        answer = 0
    return answer


A = input().upper()
B = input().upper()
print(solution(A, B))