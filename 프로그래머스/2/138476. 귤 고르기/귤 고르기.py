from itertools import permutations
from collections import Counter


def solution(k, tangerine):
    counter = dict(Counter(tangerine))
    values = sorted(list(counter.values()), reverse=True)
    
    sum = 0
    cnt = 1
    for v in values:
        sum += v
        
        
        if sum >= k:
            return cnt
        cnt += 1
        
        

