import math

def solution(n, m):
    
    def lcm(n, m):
        return (n*m) / math.gcd(n, m)
    
    
    return[ math.gcd(n, m), lcm(n, m)]