
def solution(hp):
    power = [5, 3, 1]
    count = 0
    #print(count)
    

    for p in power:
        if hp >= p:
            c, d = divmod(hp, p)
            # print(c, d)
            count += c
            hp = d
            
    return count
            
    