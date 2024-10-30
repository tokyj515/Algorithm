
import sys
input = sys.stdin.readline

from collections import defaultdict, deque
from heapq import heappush, heappop


n, m, x = map(int, input().split(" "))

graph = defaultdict(list)


for _ in range(m):
    u, v, c = map(int, input().split(" "))
    graph[u].append((v, c))


def dijkstra(start):
    dist = [float('inf') for _ in range(n + 1)]
    dist[start] = 0

    pq = []
    pq.append((0, start))

    while pq:
        cur_dist, v = heappop(pq)

        if dist[v] < cur_dist:
            continue

        for next, cost in graph[v]:
            new_dist = cur_dist + cost

            if new_dist < dist[next]:
                dist[next] = new_dist
                heappush(pq, (new_dist, next))

    return dist

# x -> 나머지
answer1 = dijkstra(x)


# 나머지 -> x
for i in range(1, n+1):
    if i == x:
        continue

    answer2 = dijkstra(i)
    answer1[i] += answer2[x]


print(max(answer1[1:]))







