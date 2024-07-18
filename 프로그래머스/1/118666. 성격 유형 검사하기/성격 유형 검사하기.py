def solution(survey, choices):
    result = ''
    cnt = {"R": 0, "T": 0, 
           "C": 0, "F": 0, 
           "J": 0, "M": 0, 
           "A": 0, "N": 0}
    
    for standard, score in zip(survey, choices):
        if score < 4 :
            cnt[standard[0]] += (4-score%4)
        elif score > 4 :
            cnt[standard[1]] += score%4
        else:
            continue
    

    
    
    if cnt['R'] >= cnt['T']:
        result += 'R'
    else:
        result += 'T'
    
    if cnt['C'] >= cnt['F']:
        result += 'C'
    else:
        result += 'F'
        
    if cnt['J'] >= cnt['M']:
        result += 'J'
    else:
        result += 'M'
    
    if cnt['A'] >= cnt['N']:
        result += 'A'
    else:
        result += 'N'
    
    
    return result
    