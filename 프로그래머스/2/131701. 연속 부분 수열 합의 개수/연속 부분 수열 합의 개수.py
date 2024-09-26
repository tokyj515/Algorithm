def solution(elements):
    
    result = set()
    # result = []
    elements_len = len(elements)
    
    for n in range(elements_len):
        now = elements[n:elements_len] + elements[:n]
        # temp = []
        
        sum = 0
        for i in range(elements_len):
            sum += now[i]
            # temp.append(sum)
            result.add(sum)
            
        # result.append(temp)
        # print(now, temp)
        
        
    # print(len(result))
    return len(result)
    
#     for row in result:
#         print(row)
    
    
    
    
    
    
    
#     # k = 1 # 수열 길이
#     i = 0 # 현재 인덱스
    
#     # 수열의 길이
#     for k in range(n+1):
        
#         while True:
#             sum = 0
#             if i +k <n-1:
#                 sum = elements[i:i+k]
#                 # result.append(sum)
#                 # i += 1
#             else:
#                 sum = elements[i]
#                 for j in range(k-1):
#                     sum += elements[j]
                
#             result.append(sum)
#             i += 1
        
        
        
#         for i in range(n):
#             sum = 0
#             if i != n-1:
#                 # sum = 0
#                 for j in range(i+1):
#                     sum += elements[i+j]
#             else:
#                 sum += elements[i]
                
#                 for j in range(i-1):
#                     sum += elements[j]
                
#             result.append(sum)
        
        
        
#         i = 0
#         sum = 0
#         cnt = 0 # 현재 인덱스에서 몇번 셌는지
#         while cnt < k:
#             sum += elements[i%n]
#             i += 1
#             cnt += 1
#         # result.add(sum)
#         result.append(sum)
        
        
        # 수열 길이 증가
        # k += 1
        
        # print(result)
            
            
        
        
        