import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
graph = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)
arr = [0] * (N + 1)  # 각 노드까지의 거리
answer = 0

# 그래프 입력
for _ in range(N - 1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# BFS 함수 정의
def bfs(start):
    queue = deque([(start, 0)])  # (현재 노드, 깊이)
    visited[start] = True

    while queue:
        v, dep = queue.popleft()
        
        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                arr[i] = arr[v] + 1  # 현재 노드의 거리 + 1
                queue.append((i, dep + 1))

# BFS 시작
bfs(1)

# 리프 노드 거리 합 계산
for i in range(2, N + 1):
    if len(graph[i]) == 1:  # 리프 노드인 경우
        answer += arr[i]

# 결과 출력 (대문자로 출력)
if answer % 2 == 1:
    print("Yes")
else:
    print("No")
