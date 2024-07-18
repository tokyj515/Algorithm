from itertools import permutations
import math


def solution(numbers):
    
    # 소수 판별 함수
    def is_prime(x):
        for i in range(2, int(math.sqrt(x)) + 1):
            if x % i == 0:
                return False
        return True 
                
    
    
    permu_list = []
    num_list = list(numbers)
    cnt = 0
    
    # 순열로 경우의 수 찾기
    for i in range(len(numbers)):
        temp = list(permutations(num_list, i+1))
        for t in temp:
            permu_list.append(t)
        
    # 중복 제거
    permu_list = list(set(permu_list))

    
    # 0으로 시작하는 경우/1만 있는 경우 제거    
    permu_new_list = []
    for x in permu_list:
        if x[0] == '1' and len(x) == 1:
            continue
        if x[0] == '0':
            continue
        permu_new_list.append(x)

        
    # 소수 찾기
    for p in permu_new_list:
        target = ''
        for i in p:
            target += i
        
        target = int(target)
        
        if is_prime(target):
            cnt += 1
            
    
    return cnt
    
    
    
    