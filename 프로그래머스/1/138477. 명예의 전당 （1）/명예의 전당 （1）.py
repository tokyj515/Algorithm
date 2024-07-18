def solution(k, score):
    result = []
    score_list = [] 
    
    for s in score:
        score_list.append(s)
        score_list.sort(reverse=True)
        
        if len(score_list) >= k:
            score_list = score_list[:k]
    
        result.append(score_list[-1])
        
    return result