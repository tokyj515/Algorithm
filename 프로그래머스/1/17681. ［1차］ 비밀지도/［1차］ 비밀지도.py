def solution(n, arr1, arr2):
    arr1_map = []
    arr2_map = []
    result = []
    
    
    def binary(num):
        b = ''
        while num > 0:
            b = str(num%2) + b 
            num //= 2
        
        if len(b) < n:
            for _ in range(n - len(b)):
                b = '0' + b
        return b
    
    
    # 구현부
    for e in arr1:
        arr1_map.append(binary(e))
    
    for e in arr2:
        arr2_map.append(binary(e))
    
    for a, b in zip(arr1_map, arr2_map):
        temp = ''
        
        for i in range(n):
            if a[i] == '0' and b[i] == '0':
                temp += " "
            else:
                temp += "#"
        
        result.append(temp)
    
    
    return result