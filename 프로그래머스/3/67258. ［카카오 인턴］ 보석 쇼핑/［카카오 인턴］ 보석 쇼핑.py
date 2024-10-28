from collections import defaultdict

def solution(gems):
    # 모든 종류의 보석을 1개씩은 포함하는 
    answer = [0, len(gems)-1]
    gems_types = len(set(gems))
    gems_cnt = defaultdict(int)
    min_val = 1000000
    
    
    start, end = 0, 0
    
    
    while end < len(gems):
        gems_cnt[gems[end]] += 1
        end += 1
        
        while len(gems_cnt) == gems_types:
            if end - start < min_val:
                min_val = end - start
                answer = [start+1, end]
                
            
            gems_cnt[gems[start]] -= 1
            if gems_cnt[gems[start]] == 0:
                del gems_cnt[gems[start]]
            start += 1
        

    
    
    return answer