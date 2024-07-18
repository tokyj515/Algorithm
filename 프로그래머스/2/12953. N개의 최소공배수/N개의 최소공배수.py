import math

def solution(arr):
    
    def lcm(a, b):
        return a*b //math.gcd(a, b)
    
    list1 = []
    
    # print(lcm(6, 8))
    
    
    temp = lcm(arr[0], arr[1])
    # list1.append(temp)
    
    for i in range(1, len(arr)-1):
        print(temp, arr[i], arr[i+1])
        if temp % arr[i+1] != 0:
            temp = lcm(temp, arr[i+1])

    
    return temp
        