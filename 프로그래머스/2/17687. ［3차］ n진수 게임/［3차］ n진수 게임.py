def solution(n, t, m, p):
    # n진법, t숫자개수, m참가인원, p튜브순서
    
    
    def convert(n, k):
        # n을 k진법으로 표현    
        result = ''
        
        while n > 0:
            if str(n % k) == '10':
                result = 'A' + result
            elif str(n % k) == '11':
                result = 'B' + result
            elif str(n % k) == '12':
                result = 'C' + result
            elif str(n % k) == '13':
                result = 'D' + result
            elif str(n % k) == '14':
                result = 'E' + result
            elif str(n % k) == '15':
                result = 'F' + result
            else:
                result = str(n % k) + result
                
            n //= k
            
        return result
    
    
    
    answer = '0' #answer의 길이 t
    result = []

    
    for i in range(1, t*m+1):
        temp = convert(i, n)
        answer += temp
    
    
#     print(answer)
#     print(answer[p-1::m])

        
        
    return answer[p-1::m][:t]
    