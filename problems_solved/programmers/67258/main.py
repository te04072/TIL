# def solution(gems):
#     N = len(set(gems))
#     L = len(gems)
#     gem_dict = {gems[0]: 1}
#     head = 0
#     tail = 0
#     min_len = L
#     if N == 1:
#         answer = (1, 1)             # 보석이 한 종류 뿐이라면 정답 고정
#     else :
#         while tail != L - 1:           
#             while True:            # 보석 종류별로 모을 때까지 루프
#                 tail += 1
#                 numT = gem_dict.get(gems[tail], 0) + 1  # 새로운 보석 구매
#                 gem_dict.update({gems[tail]:numT})
#                 if len(gem_dict.keys()) == N:
#                     break
#             while len(gem_dict.keys()) == N:
#                 numH = gem_dict.get(gems[head])
#                 if numH != 1:                           # 배열 head의 보석이 두 개 이상이라면
#                     gem_dict.update({gems[head]:(numH - 1)})    # 보석 제외, head 1 증가
#                     head += 1
#                 else:
#                     break
#             if tail - head < min_len:                       # 기존 최단구간보다 구간길이가 짧다면
#                 min_len = tail - head
#                 answer = head + 1, tail + 1                 # 인덱스 고려하여 보정
#     return answer

ls = ["XYZ", "XYZ", "XYZ"]
print(solution(ls))