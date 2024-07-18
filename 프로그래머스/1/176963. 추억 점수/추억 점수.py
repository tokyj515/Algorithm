def solution(name, yearning, photo):
    # 이름
    # 각 사람별 그리움 점수
    # 사진에 담긴 이름
    answer = []
    
    score = {}
    
    for n, y in zip(name, yearning):
        score[n] = y

    for ph in photo:
        sum = 0
        for p in ph:
            if p in list(score.keys()):
                sum += score[p]
            else:
                continue
        answer.append(sum)
        
        
    return answer
        
            
        
        