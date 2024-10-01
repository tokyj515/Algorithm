from collections import Counter

def solution(want, number, discount):
    
    # 할인은 10일동안 진행, 할인 제품은 하루에 하나
    # 
    
    answer = 0
    discount_len = len(discount)
    
    
    for i in range(discount_len-10+1):
        arr = discount[i:i+10]
        
        counter = Counter(arr)
        
        flag = True
        
        for w, n in zip(want, number):
            if counter[w] != n:
                flag = False
        
        if flag:
            # print(counter)
            answer += 1
    
    
    
    
    return answer