# T = int(input())
# for tc in range(1, T+1):
#     N, M = map(int, input().split())
#     weights = sorted(list(map(int, input().split())), reverse=True)      # 화물, 트럭 내림차순 정렬
#     trucks = sorted(list(map(int, input().split())), reverse=True)
#     idx = 0
#     output = 0
#     for i in range(M):
#         while idx < N:
#             if trucks[i] >= weights[idx]:
#                 output += weights[idx]          # 순서대로 적재 가능한 최대 중량 발견 시 무게 합산
#                 idx += 1
#                 break
#             else:
#                 idx += 1
#     print(f"#{tc} {output}")

# def check_run(ls):
#     for idx in range(8):
#         if ls[idx] and ls[idx+1] and ls[idx+2]:
#             return True
#     else:
#         return False
#
#
# def check_triplet(ls):
#     for idx in range(10):
#         if ls[idx] >= 3:
#             return True
#     else:
#         return False
#
#
# T = int(input())
# for tc in range(1, T+1):
#     cards = list(map(int, input().split()))
#     player_1 = [0]*10
#     player_2 = [0]*10
#     output = 0
#     for i in range(6):
#         player_1[cards[i*2]] += 1
#         player_2[cards[1+i*2]] += 1
#         if i >= 2:
#             if check_run(player_1) or check_triplet(player_1):
#                 output = 1
#                 break
#             elif check_run(player_2) or check_triplet(player_2):
#                 output = 2
#                 break
#     print(f"#{tc} {output}")


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    trucks = [list(map(int, input().split())) for __ in range(N)]
    target = trucks + []
    timetable = [0]*24
    output = 0
    order = [i for i in range(N)]
    for i in range(N):
        for j in range(0, N-i-1):
            if target[j][1] - target[j][0] > target[j + 1][1] - target[j + 1][0]:
                target[j], target[j + 1] = target[j + 1], target[j]
    for k in range(N):
        start_time = target[k][0]
        end_time = target[k][1]
        if timetable[start_time:end_time] == [0] * (end_time - start_time):
            for m in range(start_time, end_time):
                timetable[m] += 1
            output += 1
        else:
            continue
    print(f"#{tc} {output}")