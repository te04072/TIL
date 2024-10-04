from collections import deque
cacheSize = int(input())
string = input()
cities = []
temp = ''
status = False
for char in string:                 # string에서 cities 추출
    if char.isalpha():
        temp += char
        status = True
    elif status and not char.isalpha():
        cities.append(temp.upper())     # 특수문자 사이의 영단어를 대문자로 변경 후 리스트에 추가
        temp = ''
        status = False

stored = 0
output = 0
cache = deque()
for city in cities:
    if city in cache:           # cache에 저장된 도시라면 1초 소요, 최근 순서로 갱신
        output += 1
        cache.remove(city)
        cache.append(city)
    elif city not in cache and stored < cacheSize:  # cache에 없는 도시가 나왔고 빈 공간이 남아있다면
        stored += 1                                 # cache에 새로 저장
        output += 5
        cache.append(city)
    else:
        output += 5                                 # cache에 없는 도시가 나왔고 공간이 꽉 찼다면
        if cache:
            cache.popleft()                             # 나온지 가장 오래된 도시 pop 후 새 도시 추가
            cache.append(city)
print(output)

# def solution(cacheSize, cities):
#     stored = 0
#     answer = 0
#     cache = deque()
#     for city in cities:
#             city = city.upper()
#             if city in cache:           # cache에 저장된 도시라면 1초 소요, 최근 순서로 갱신
#                 answer += 1
#                 cache.remove(city)
#                 cache.append(city)
#             elif city not in cache and stored < cacheSize:  # cache에 없는 도시가 나왔고 빈 공간이 남아있다면
#                 stored += 1                                 # cache에 새로 저장
#                 answer += 5
#                 cache.append(city)
#             else:
#                 answer += 5                                 # cache에 없는 도시가 나왔고 공간이 꽉 찼다면
#                 if cache:
#                     cache.popleft()                             # 나온지 가장 오래된 도시 pop 후 새 도시 추가
#                     cache.append(city)
#
#     return answer

