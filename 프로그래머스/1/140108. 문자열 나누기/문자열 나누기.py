from collections import defaultdict

def solution(s):
    # answer = []
    answer = 0
    # s = 'abaaaaaabbba'
    
    while len(s) > 1:
        # counter = {}
        x = s[0]
        x_count = 0
        else_count = 0
        
        
        for i, e in enumerate(s):
            if e == x:
                x_count += 1
            else:
                else_count += 1
            
            
            if x_count == else_count:
                # answer.append(s[:i+1])
                answer += 1
                s = s[i+1:]
                
                # print(answer)
                
                break
                
        if x_count > else_count:
            return answer + 1
                
    if len(s) == 1:
        answer += 1
    
    return answer