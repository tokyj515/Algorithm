def solution(array, commands):
    answer = []
    
    for c in commands:
        i = c[0]
        j = c[1]
        k = c[2]
        
        slice_list = array[i-1:j]
        slice_list.sort()

        
        answer.append(slice_list[k-1])
    
    
    return answer