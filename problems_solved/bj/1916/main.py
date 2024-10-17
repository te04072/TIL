# bj 1916

import heapq

INF = 1e8               # float('inf')보다 시간 단축
N = int(input())
M = int(input())
distance = [[INF]*(N+1) for __ in range(N+1)]
cities = [INF]*(N+1)
visited = [0]*(N+1)
for i in range(N+1):
    distance[i][i] = 0
for __ in range(M):
    s, e, d = map(int, input().split())
    distance[s][e] = min(distance[s][e], d)      # 거리 정보 입력 : 간선이 여러 개일 경우 작은 쪽을 선택!!

s, e = map(int, input().split())                            # dijkstra
pq = []
heapq.heappush(pq, (0, s))
cities[s] = 0

while pq:
    dist, cur = heapq.heappop(pq)
    if visited[cur]:
        continue
    visited[cur] = 1

    for nxt in range(1, N+1):
        if distance[cur][nxt] != INF:
            temp = dist + distance[cur][nxt]
            if temp < cities[nxt]:
                cities[nxt] = temp
                heapq.heappush(pq, (temp, nxt))

print(cities[e])
