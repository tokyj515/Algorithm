from collections import Counter

def solution(topping):
    # 토핑 종류의 수가 동일하면 공평한 것
    answer = 0
    
    left = {}
    right = Counter(topping)

    
    for t in topping:
        
        if t not in left:
            left[t] = 1
        else:
            left[t] += 1
        right[t] -= 1
        
        
        if right[t] == 0:
            del right[t]
        
        
        if len(left) == len(right):
            answer += 1
    
    return answer
        
    
        
        
        
        
        