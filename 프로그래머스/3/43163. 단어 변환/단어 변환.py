import copy

def solution(begin, target, words):
    
    if target not in words:
        return 0
    
    
    result = []
    answer = []
    visited = [0 for _ in range(len(words))]

    cnt = 100
    
    
    def can_change(now, word):
        
        cnt = 0
        
        for i, j in zip(now, word):
            if i != j:
                cnt += 1
        
        if cnt > 1:
            return False
        return True
    
    
    
    def backtrack(dep, now):
        nonlocal cnt
        
        if now == target:
            cnt = min(cnt, dep)
            temp = answer[::]
            result.append(temp)
            # print(temp)
            return
        
        
        for i, w in enumerate(words):
            if not visited[i] and can_change(now, w):
                answer.append(w)
                visited[i] = 1
                backtrack(dep+1, w)
                answer.pop()
                visited[i] = 0
        
        
        
        
        
    backtrack(0, begin)
    
    return cnt