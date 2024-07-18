from itertools import permutations

def solution(numbers):
    permu_list = list(permutations(numbers, 2))
    
    answer = []
    
    
    for p in permu_list:
        temp = sum(p)
        answer.append(temp)
        
    
    answer = list(set(answer))
    answer.sort()
    
    return answer