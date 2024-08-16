from collections import deque

# def generator(ls):
#     for i in range(5):
#         ls[0] -= i + 1
#         ls = ls[1:]+[ls[0]]
#         if ls[-1] <= 0:
#             ls[-1] = 0
#             break
#     return ls
#
#
# for test_case in range(1, 11):
#     tc = int(input())
#     numbers = list(map(int, input().split()))
#     while numbers[7] != 0:
#         numbers = generator(numbers)
#     print(f"#{tc}", end=" "), print(*numbers)
#
# # queue
# for test_case in range(1, 11):
#     tc = int(input())
#     numbers = list(map(int, input().split()))
#     target = deque()
#     for i in range(8):
#         target.append(numbers[i])
#     while target[-1] != 0:
#         for j in range(1, 6):
#             temp = target.popleft() - j
#             target.append(temp)
#             if temp <= 0:
#                 target[-1] = 0
#                 break
#     print(f"#{tc}", end=" "), print(*target)
#
#
# T = int(input())
# for test_case in range(1, T+1):
#     N, M = map(int, input().split())
#     target = list(map(int, input().split()))
#     index = M % N
#     print(f"#{test_case} {target[index]}")
#
# # queue
# T = int(input())
# for test_case in range(1, T+1):
#     N, M = map(int, input().split())
#     num_list = list(map(int, input().split()))
#     target = deque()
#     for i in range(N):
#         target.append(num_list[i])
#     for __ in range(M):
#         temp = target.popleft()
#         target.append(temp)
#     print(f"#{test_case} {target[0]}")

# T = int(input())
# for test_case in range(1, T+1):
#     N, M = map(int, input().split())
#     pizzas = list(map(int, input().split()))
#     pizzas = [[pizzas[i], i] for i in range(M)]
#     oven = deque()
#     for i in range(N):
#         oven.append(pizzas[i])
#     pizzas = pizzas[M:N-1:-1]
#     cnt = 0
#
#     while oven:
#         if len(oven) == 1:  # 녹는시점주의
#             break
#         temp = oven.popleft()
#         if temp[0] == 0:
#             if pizzas:
#                 new_pizza = pizzas.pop()
#                 oven.appendleft(new_pizza)
#         else:
#             temp[0] //= 2
#             oven.append(temp)
#     output = oven.pop()[1] + 1
#     print(f"#{test_case} {output}")

# without deque
T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    pizzas = list(map(int, input().split()))        # 치즈 양 따로 저장
    oven = [i for i in range(N)]                    # 오븐에는 인덱스만
    visited = [1]*N + [0]*(M-N)
    cur = 0                                         # 체크포인트
    output = None
    while oven:
        if pizzas[oven[cur]] == 0:                        # 체크포인트에서 치즈가 0이 되었다면 0이 아닌 피자 인덱스를 입력
            for j in range(M):
                if visited[j] == 1:                       # 오븐에 넣지 않은 피자 찾기
                    continue
                if pizzas[j] != 0:
                    oven[cur] = j
                    visited[j] = 1                                      # 체크포인트 이동하지 않고 바로 새 피자 while 루프
                    break
            else:
                if len(oven) == 2:              # cur 치즈가 0이고 오븐에 피자 두 개가 남았다면 마지막 피자번호 계산 후 break
                    output = oven[(cur + 1) % 2] + 1
                    break
                elif visited == [1]*M:
                    oven.pop(cur)               # 추가할 피자가 없다면 오븐에서 꺼내기만, 체크포인트 이동할 필요 x
                    cur %= len(oven)
        else:
            pizzas[oven[cur]] //= 2                   # 다시 넣은 피자 치즈 녹이기
            cur = (cur + 1) % len(oven)
    print(f"#{test_case} {output}")


