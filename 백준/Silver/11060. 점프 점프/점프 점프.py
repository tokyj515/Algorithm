
import sys
input = sys.stdin.readline

from collections import deque


N = int(input())
arr = list(map(int, input().split(" ")))

move = [10000000 for _ in range(N)]
visited = [0 for _ in range(N)]

def bfs(start):
    queue = deque()

    visited[start] = 1
    queue.append(start)
    move[start] = 0

    while queue:
        v = queue.popleft()

        for next in range(v+1,  min(v + arr[v] + 1, N)):
            if not visited[next]:
                visited[next] = 1
                queue.append(next)
                move[next] = min(move[next], move[v]+1)



bfs(0)

# print(move)
if move[-1] == 10000000:
    print(-1)
else:
    print(move[-1])