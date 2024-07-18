# 입력된 세로<가로

def solution(sizes):
    answer = 0

    for i in range(len(sizes)):
        w, h = sizes[i]
        if w < h:
            sizes[i] = [h, w]
  
  
    print(sizes)  
    
    
    w_list = [e[0] for e in sizes]
    h_list = [e[1] for e in sizes]
    
    print(w_list, h_list)
    
    return max(w_list) * max(h_list)
    
