from collections import defaultdict, deque


def solution(n, computers):
    graph = defaultdict(set)
    visited = [0 for i in range(n)]
    
    cnt = 0
    
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if computers[i][j] == 1:
                graph[i].add(j)
                graph[j].add(i)

                
                
                
    def bfs(start):
        queue = deque()
        queue.append(start)
        visited[start] = 1
        
        while queue:
            v = queue.popleft()
            
            for i in graph[v]:
                if not visited[i]:
                    visited[i] = 1
                    queue.append(i)
                    
    
    
    for i in range(n):
        if not visited[i]:
            bfs(i)
            cnt += 1
    

    
    return cnt
        
        
        
        
        