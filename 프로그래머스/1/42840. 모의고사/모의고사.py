def solution(answers):

    p1 = [1, 2, 3, 4, 5]
    p2 = [2, 1, 2, 3, 2, 4, 2, 5]
    p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    correct = {1:0, 2:0, 3:0}
    
    for i, a in enumerate(answers):
        if p1[i % 5] == a:
            correct[1] += 1
        
        if p2[i % 8] == a:
            correct[2] += 1
        
        if p3[i % 10] == a:
            correct[3] += 1
            

    max_correct = max(correct.values())
    result = []
    
    for k, v in correct.items():
        if v == max_correct:
            result.append(k)
            
    result.sort()
    
    
    return result
    

            
            