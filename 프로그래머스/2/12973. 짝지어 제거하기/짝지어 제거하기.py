from collections import deque

def solution(s):
    alp = list(s)
    stack = []
    stack.append(alp[0])
    alp.pop(0)
    

    for a in alp:
        if stack and stack[-1] == a:
            stack.pop()
            
        else:
            stack.append(a)
    
    
    if stack:
        return 0
    else:
        return 1
    