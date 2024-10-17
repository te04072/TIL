from collections import deque
M, N = map(int, input().split())
tomatoes = [list(map(int, input().split())) for _ in range(N)]
past_tomatoes = [[0]*M for __ in range(N)]
target = 0
output = 0
delta = [[1, 0], [0, -1], [-1, 0], [0, 1]]
deq = deque()
for i in range(N):
    for j in range(M):
        if tomatoes[i][j] == 0:
            target += 1             # 익지 않은 토마토의 수 저장
        elif tomatoes[i][j] == 1:
            deq.append(i)           # 익은 토마토의 좌표 큐에 저장
            deq.append(j)
if target == 0:
    output = 0
while target:
    temp = target
    ripe = len(deq)//2
    for t in range(ripe):
        tmt_i = deq.popleft()
        tmt_j = deq.popleft()
        for d in delta:
            nxt_i = tmt_i + d[0]
            nxt_j = tmt_j + d[1]
            if 0 <= nxt_i < N and 0 <= nxt_j < M and tomatoes[nxt_i][nxt_j] == 0:   # 인덱스 범위 내에서 델타탐색
                tomatoes[nxt_i][nxt_j] = 1
                deq.append(nxt_i)       # 익은 토마토는 다음 루프 순회 대상으로 저장
                deq.append(nxt_j)
                target -= 1
    if target and temp == target:       # 토마토가 남아있지만 for loop 전후로 변화가 없었다면 break
        output = -1
        break
    else:
        output += 1
print(output)
