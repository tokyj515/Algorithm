def solution(num, total):
    result = []
    
    a = int((total*2/num-num+1)/2)
    
    for i in range(a, a+num):
        result.append(i)
    
#     if num % 2 ==1:
#         mid = int(total/num)
#         offset = num //2
        
#         for i in range(mid-offset, mid+offset+1):
#             result.append(i)
            
#     else:
#         mid = total//2 //2
        
#         result.append(mid)
#         result.append(mid+1)

#         while len(result) != num:
#             result.append(result[0]-1)
#             result.sort()
#             result.append(result[-1]+1)
        
        
        
            
    
    
    return result