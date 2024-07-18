def solution(n):
    n_list = [x for x in list(str(n))]
    n_list.sort(reverse=True)
    
    return int("".join(n_list))