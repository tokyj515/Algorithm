
from collections import deque

def solution(priorities, location):
    
    max_val = max(priorities)
    my = (location, priorities[location])
    priorities = deque(enumerate(priorities))
    answer = []

    
    while priorities:
        print(answer)
        i, p = priorities.popleft()
        
        if priorities and p < max(p for i, p in priorities):
            priorities.append((i, p))
        else:
            answer.append((i, p))
            
#     print(my)
#     print(answer)
    
    for i, element in enumerate(answer):
        if my == element:
            return i+1
    
