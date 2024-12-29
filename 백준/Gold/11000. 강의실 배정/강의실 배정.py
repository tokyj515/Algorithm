
import sys
input = sys.stdin.readline

from heapq import heappush, heappop

N = int(input())
time = []
pq = []

for _ in range(N):
    a, b = map(int, input().split(" "))
    time.append([a, b])

time.sort()

heappush(pq, time[0][1])


for i in range(1, N):
    if pq[0] <= time[i][0]:
        heappop(pq)
    heappush(pq, time[i][1])


print(len(pq))