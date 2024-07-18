def solution(n):
    num = []
    
    i = 1
    
    while len(num) <= 100:
        if i % 3 != 0 and '3' not in str(i):
            num.append(i)
            
        i += 1
        
    return num[n-1]