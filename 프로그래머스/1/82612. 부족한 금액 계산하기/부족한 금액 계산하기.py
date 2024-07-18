def solution(price, money, count):
    
    sum = 0
    
    for i in range(count):
        sum += price * (i+1)
    
    
    if sum - money > 0:
        return sum - money
    else:
        return 0