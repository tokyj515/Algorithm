T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    
    graph = [[0 for _ in range(n)] for _ in range(n)]

    
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    
    d = 0
    x = 0
    y = 0
    
    
  
    graph[x][y] = 1
    
    for i in range(2, n*n+1): 
        
        nx = x + dx[d]
        ny = y + dy[d]
        
        if not (0<= nx and nx < n and 0<=ny and ny < n) or graph[nx][ny] != 0:
            d = (d+1)%4
           
        x = x + dx[d]
        y = y + dy[d]
        
        graph[x][y] = i

        #print(f"{x}, {y} -> {d}") 
    
    
    print("#{}".format(test_case))  
    
    for row in graph:
         print(*row)