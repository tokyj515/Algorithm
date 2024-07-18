def solution(sides):
    # 만들 수 있으면 1
    # 만들 수 없으면 2
    
    sides.sort()
    
    if sides[2] < sides[1] + sides[0]:
        return 1
    else: 
        return 2
    