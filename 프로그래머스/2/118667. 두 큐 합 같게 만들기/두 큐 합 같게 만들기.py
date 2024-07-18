from collections import deque

def solution(queue1, queue2):
    sum_val = sum(queue1) + sum(queue2)
    
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    
    A = sum(queue1)
    B = sum(queue2)
    answer = 0
    
    limit = len(queue1) * 3
    
    
    while A != B:
        
        if A > B:
            temp =  queue1.popleft()
            queue2.append(temp)
            A -= temp
            B += temp
                
        elif A < B:
            temp =  queue2.popleft()
            queue1.append(temp)
            A += temp
            B -= temp

            
        answer += 1    
        
        if answer == limit:
            return -1
            
    
    
    
    return answer
            