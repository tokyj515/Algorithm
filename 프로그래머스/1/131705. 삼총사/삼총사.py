# 3명의 정수 번호를 합하면 0 -> 삼총사
# 삼총사를 만들 수 있는 방법
# 1번 dfs
# 2번 순열

from itertools import permutations
from itertools import combinations

def solution(number):
    result = 0
    
    com_list = list(combinations(number, 3))
    
    print(com_list)
    
    for e in com_list:
        if sum(e) == 0:
            result += 1
    
    
    return result
    
    
    
#     answer = 0 # 중간에 3이 되는지
#     visited = [0 for _i in range(len(number))]
#     result = 0 # 삼총사 개수
    

    
    
#     def dfs(i, answer, number, visited):
#         global result
        
#         # 현재 인덱스 방문하고 그 값을 answer에 더해
#         visited[i] = 1
#         answer += number[i]
        
#         # answer가 되면 삼총사 개수에 추가
#         if answer == 3:
#             result += 1
#             answer = 0
        
#         if visited[i+1] == 0:
#             dfs(i+1)

#     dfs(0, 0, number, visited) #시작 인덱스0, answer가 3이 되는지
    
    
#     return result
    
    
        