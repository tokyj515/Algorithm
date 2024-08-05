from itertools import combinations

def solution(clothes):
    
    kinds = {} 
    
    cnt = 1
    
    for c in clothes:
        if c[1] not in kinds.keys():
            kinds[c[1]] = [[]]
        kinds[c[1]].append(c[0])
        
    print(kinds)
    
    
    # 각 종류의 경우의 수 다 곱하기
#     for k in kinds.keys():
#         cnt *= len(kinds[k])
#     # print(cnt)
    
        
#     # 각 분야에서 하나씩만 입을 때
#     if len(kinds.keys()) > 1: 
#         for k in kinds.keys():
#             cnt += len(kinds[k])
        
    # print(cnt)
    
    
    for k in kinds.keys():
        cnt *= len(kinds[k])
    
    return cnt - 1

        
    