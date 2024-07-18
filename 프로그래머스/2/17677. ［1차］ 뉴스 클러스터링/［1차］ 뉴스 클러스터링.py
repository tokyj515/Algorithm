from collections import Counter


def solution(str1, str2):
    # J(A, B) -> 교집합 크기 / 합집합 크기
    # A와 B가 공집합이면 1

    str1_list = []
    str2_list = []

    
    for i in range(len(str1)-1):
        temp = str1[i] + str1[i+1]
        if temp.isalpha():
            str1_list.append(temp.lower())
    
    for i in range(len(str2)-1):
        temp = str2[i] + str2[i+1]
        if temp.isalpha():
            str2_list.append(temp.lower())
        
    print(str1_list, str2_list)
    
    
    # 요소가 몇개씩 있는지
    element = set(str1_list+str2_list)
    
    str1_counter = dict(Counter(str1_list))
    str2_counter = dict(Counter(str2_list))
    
    print(str1_counter, str2_counter)
    print(element)
    
    
    # 합집합
    uni = 0
    inter = 0
    
    for e in element:
        if e in str1_counter.keys() and e in str2_counter.keys():
            max_val = max(str1_counter[e], str2_counter[e])
            min_val = min(str1_counter[e], str2_counter[e])
            uni += max_val
            inter += min_val
        elif e in str1_counter.keys():
            max_val = str1_counter[e]
            min_val = 0
            uni += max_val
            inter += min_val
        elif e in str2_counter.keys():
            max_val = str2_counter[e]
            min_val = 0
            uni += max_val
            inter += min_val
            
            
    if uni == 0 and inter == 0:
        return 65536
    else:
        return int(inter/uni*65536)
    #elif inter
    

    