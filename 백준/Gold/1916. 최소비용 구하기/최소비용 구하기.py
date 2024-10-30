

import sys
input = sys.stdin.readline

from collections import defaultdict
from heapq import heappush, heappop


N = int(input())
M = int(input())

graph = defaultdict(list)

for _  in range(M):
    u, v, w = map(int, input().split(" "))
    graph[u].append((v, w))

start, end = map(int, input().split(" "))


def dijkstra(start):
    dist = [float('inf') for _ in range(N+1)]
    pq = []

    dist[start] = 0
    pq.append((0, start))


    while pq:
        cd, cv = heappop(pq)    # 현재 거리, 현재 노드

        if dist[cv] < cd:   # 현재 노드에 기록된 거리, 원래 거리
            continue


        for next, weight in graph[cv]:
            new_dist = dist[cv] + weight

            if dist[next] > new_dist:
                dist[next] = new_dist
                heappush(pq, (new_dist, next))

    return dist

answer = dijkstra(start)
print(answer[end])