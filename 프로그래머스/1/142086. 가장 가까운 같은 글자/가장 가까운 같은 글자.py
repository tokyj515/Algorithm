def solution(s):
    # s_list = list(s)
    result = []
    
    for i, n in enumerate(s):
        temp = s[0:i]
        # print(temp)
        
        if n not in temp:
            result.append(-1)
        else:
            idx = temp.rindex(n)
            result.append(i-idx)
            
    return result