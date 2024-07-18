from collections import deque

def solution(s):
    answer = []
    s_list = []
    
    # 대괄호 삭제 -> 리스트화
    for e in s.split("},"):
        e = e.replace("{{", "")
        e = e.replace("{", "")
        e = e.replace("}}", "")      
        s_list.append(e.split(","))
        
        
    s_list.sort(key=len)


    for s in s_list:
        for e in s:
            if e not in answer:
                answer.append(e)
                
    answer = list(map(int, answer))
                
    return answer
