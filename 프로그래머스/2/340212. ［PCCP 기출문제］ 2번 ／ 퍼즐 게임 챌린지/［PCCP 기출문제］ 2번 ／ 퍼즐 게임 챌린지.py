def solution(diffs, times, limit):
    N = len(diffs)
    
    
    
    left = 1
    right = max(diffs)
    level = right
    
    
    while left <= right:
        mid = (left+right)//2   # mid는 계산할 level,
    
        now_total = 0
    
    
        for i in range(N):
            now_diff = diffs[i]
            now_times = times[i]
            
            if i > 0:
                prev_time = times[i-1]
            else:
                prev_time = 0

            
            
            if now_diff <= mid:
                now_total += now_times
            
            else:
                now_total += (now_times+prev_time)*(now_diff - mid) + now_times
                
        
        if now_total <= limit: # 더 낮출 수 있으면 낮추기
            level = mid
            right = mid -1
    
        else:
            left = mid + 1
            
    return level
    
        
        