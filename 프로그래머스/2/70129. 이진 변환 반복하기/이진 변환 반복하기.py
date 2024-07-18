def solution(s):
    cnt = 0
    zero = 0
    
    def binary(n):
        res = ""
        while n > 0:
            res = str(n % 2) + res
            n //= 2
        return res
    


    

    while s != "1":   
        n = s.count("0")
        s = s.replace("0", "")
        s = binary(int(len(s)))
        
        cnt += 1
        zero += n

        
    return [cnt, zero]
    