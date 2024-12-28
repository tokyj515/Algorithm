from collections import deque, defaultdict


def solution(n, edge):
    graph = defaultdict(list)
    dep = [0 for _ in range(n+1)]
    
    
    for u, v in edge:
        graph[u].append(v)
        graph[v].append(u)
        
    
    def bfs(start):
        queue = deque()
        visited = [0 for _ in range(n+1)]
        
        
        queue.append(start)
        visited[start] = 1
        dep[start] = 1
        
        while queue:
            v = queue.popleft()
            
            for next in graph[v]:
                if not visited[next]:
                    queue.append(next)
                    visited[next] = 1
                    dep[next] = dep[v]+1
    
    
    bfs(1)
    
    max_val = max(dep)
    
    cnt = 0
    for i in dep:
        if i == max_val:
            cnt += 1
            
    
    return cnt
        
        