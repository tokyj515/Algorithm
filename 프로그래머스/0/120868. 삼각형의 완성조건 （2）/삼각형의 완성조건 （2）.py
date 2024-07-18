def solution(sides):
    answer = []

    # sides에 가장 긴 변이 있는 경우
    a = max(sides)
    b = min(sides)
    
    for i in range(a-b+1, a+b):
        answer.append(i)
    
    return len(answer)