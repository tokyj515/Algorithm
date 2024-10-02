import sys
from collections import deque
input = sys.stdin.readline


n = int(input())
arr = list(map(int, input().split(" ")))
visited = [-1 for _ in range(n)]

queue = deque()

# 0인덱스에 1뎁스
queue.append([0, 0])
visited[0] = 0


while queue:
    i, dep = queue.popleft()

    dist = arr[i]

    for j in range(1, dist+1):
        if i+j < n:
            if visited[i+j] == -1:
                visited[i+j] = dep+1
                queue.append([i + j, dep + 1])


    if visited[-1] != -1:
        break

if visited[n-1] == -1:
    print(-1)
else:
    print(visited[n-1])



