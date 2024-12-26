
def solution(begin, target, words):
    
    if target not in words:
        return 0
    
    
    
    answer = []
    result = []
    visited = [0 for _ in range(len(words))]
    cnt = 100
    
    
    def can_change(a, b):
        differ = 0
        
        for i, j in zip(a, b):
            if i != j:
                differ += 1
        
        return differ == 1
        
        
    
    def backtrack(word, dep):
        
        nonlocal cnt
        
        if word == target:
            temp = answer[::]
            result.append(temp)
            cnt = min(cnt, dep)
            return
        
        
        for i, next in enumerate(words):
            if can_change(word, next) and not visited[i]:
                visited[i] = 1
                answer.append(next)
                backtrack(next, dep+1)
                visited[i] = 0
                answer.pop()
            
    
    backtrack(begin, 0)
    
    
    return cnt
    