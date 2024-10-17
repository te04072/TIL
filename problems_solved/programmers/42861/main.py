import heapq
from collections import defaultdict

def solution(n, costs):
    graph = defaultdict(list)
    for cost in costs:
        s, e, d = cost[0], cost[1], cost[2]
        graph[s].append((e, d))
        graph[e].append((s, d))
    visited = [0] * n
    min_graph = [[0] * n for __ in range(n)]
    min_node = [-1] * n

    pq = [(0, 0, 0)]
    while pq:
        dist, cur, pri = heapq.heappop(pq)
        if visited[cur]:
            continue
        visited[cur] = 1
        min_graph[cur][pri] = 1
        min_graph[pri][cur] = 1
        min_node[cur] = dist
        for n, d in graph[cur]:
            if not visited[n]:
                heapq.heappush(pq, (d, n, cur))
    answer = sum(min_node)
    return answer