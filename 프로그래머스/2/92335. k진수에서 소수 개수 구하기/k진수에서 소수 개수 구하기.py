import math

def solution(n, k):
    def convert(n, k):
        result = ''
        
        while n > 0:
            result = str(n%k) + result
            n //= k
        
        return result
    
    
    def is_prime(n):
        if n < 2:
            return False
        
        for i in range(2, int(math.sqrt(n))+1):
            if n % i == 0:
                return False
        return True
    

    
    num = convert(n, k)
    result = 0
    

    num_list = num.split('0')
    print(num_list)
    
    for n in num_list:
        if n == '':
            continue 
        if is_prime(int(n)):
            result += 1
    
    
    
    return result
    
    
        
    