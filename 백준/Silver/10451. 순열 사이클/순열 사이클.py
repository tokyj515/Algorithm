import sys
sys.setrecursionlimit(10**6)



def dfs(graph, visited, v):
    visited[v] = 1

    for i in graph[v]:
        if not visited[i]:
            dfs(graph, visited, i)




answer = []
tc = int(sys.stdin.readline())

for _ in range(tc):

    num = int(sys.stdin.readline())
    temp = [int(x) for x in sys.stdin.readline().split(" ")]

    graph = [[] for _ in range(num+1)]
    visited = [0] * (num+1)

    for i in range(1, len(graph)):
        graph[i].append(temp[i-1])
        # graph[temp[i - 1]].append(i)


    cnt = 0
    for i in range(1, len(graph)):
        if not visited[i]:
            dfs(graph, visited, i)
            cnt += 1


    print(cnt)
