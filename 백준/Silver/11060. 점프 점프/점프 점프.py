import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

queue = deque()
visited = [-1] * n  # 각 위치에 도달하는 최소 depth를 저장

# 시작점(0)에서 depth 1
queue.append((0, 0))
visited[0] = 0  # 시작점에 대한 방문 처리

while queue:
    i, dep = queue.popleft()
    
    # 현재 위치에서 최대 arr[i]만큼 이동할 수 있음
    for j in range(1, arr[i] + 1):  # j는 1부터 arr[i]까지
        next_idx = i + j
        
        # 범위 체크
        if next_idx >= n:
            continue
        
        # 방문하지 않은 곳이면 큐에 추가하고 depth 갱신
        if visited[next_idx] == -1:
            visited[next_idx] = dep + 1
            queue.append((next_idx, dep + 1))
    
    # 목적지에 도달하면 바로 종료
    if visited[n-1] != -1:
        break

# 결과 출력
if visited[n-1] == -1:
    print(-1)  # 도달할 수 없는 경우
else:
    print(visited[n-1])  # 도달한 최소 횟수
