def solution(n,a,b):
    round = 0
    
    while a != b: # 둘다 1이 되는 순간 멈춤
        round += 1
        a, b = (a+1)//2, (b+1)//2
            
    return round

    