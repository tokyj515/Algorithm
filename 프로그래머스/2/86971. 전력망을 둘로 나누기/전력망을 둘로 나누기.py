from collections import defaultdict, deque

def solution(n, wires):
    def bfs(start, visited):
        queue = deque([start])
        visited[start] = 1
        count = 1  

        while queue:
            node = queue.popleft()
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    visited[neighbor] = 1
                    queue.append(neighbor)
                    count += 1 
        return count

    answer = float('inf')  
    N = len(wires)

    
    for ex in range(N):
        graph = defaultdict(list)
        for i in range(N):
            if i == ex:  # 간선 제외
                continue
            u, v = wires[i]
            graph[u].append(v)
            graph[v].append(u)

        visited = [0] * (n + 1) 
        sizes = []

        for i in range(1, n + 1):  
            if not visited[i]:
                sizes.append(bfs(i, visited))


        if len(sizes) == 2:
            diff = abs(sizes[0] - sizes[1])
            answer = min(answer, diff)  # 최소값 갱신

    return answer
