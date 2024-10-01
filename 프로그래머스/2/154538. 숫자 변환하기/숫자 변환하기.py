from collections import deque

def solution(x, y, n):
    result = 1000000
    queue = deque()
    
    visited = set()
    
    queue.append([x, 0])
    
    while queue:
        num, dep = queue.popleft()
    
        if num == y:
            return dep
        
        if num > y or num in visited:
            continue
        
        
        visited.add(num)
        
        queue.append([num+n, dep+1])
        queue.append([num*2, dep+1])
        queue.append([num*3, dep+1])
    
    
    
    return -1  
    
    
    
    
#     if result == 1000000:
#         return -1
#     else:
#         return result