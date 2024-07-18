from itertools import permutations

def solution(spell, dic):
    permu_list = []
    case = []
    
    
    for p in list(permutations(spell, len(spell))):
        p = list(p)
        permu_list.append("".join(p))
    
    for p in permu_list:
        if p in dic:
            return 1
    
    
    return 2
        
    