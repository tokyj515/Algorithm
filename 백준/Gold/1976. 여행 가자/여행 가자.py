

from collections import defaultdict, deque



N = int(input())
M = int(input())


temp = []
for _ in range(N):
    t = list(map(int, input().split(" ")))
    temp.append(t)

plan = list(map(int, input().split(" ")))


graph = defaultdict(set)

for i in range(N):
    for j in range(N):
        if temp[i][j] == 1:
            graph[i+1].add(j+1)
            graph[j+1].add(i+1)



def bfs(start, end):
    queue = deque()
    visited = []
    queue.append(start)
    visited.append(start)


    while queue:
        v = queue.popleft()

        if v == end:
            return True

        for i in graph[v]:
            if i not in visited:
                queue.append(i)
                visited.append(i)
                

    return False


def is_connected():
    start = plan[0]
    cities = plan[1:]

    for c in cities:
        if not bfs(start, c):
            return False
    return True




if is_connected():
    print("YES")
else:
    print("NO")

