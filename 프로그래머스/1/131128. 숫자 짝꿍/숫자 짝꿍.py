def solution(X, Y):
    answer = ''

    pair = []
    num = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]


    for z in num:
        if (z in X) and (z in Y):  # and(z not in pair)
            
            count = 0
            if X.count(z)>Y.count(z):
                count = Y.count(z)
            else: 
                count = X.count(z)
                
            for _ in range(count):
                pair.append(z)

                
                
    if not pair:
        return "-1"
    elif len(pair) == pair.count("0"):
        return "0"
    else:
        pair.sort(reverse=True)
        for e in pair:
            answer += e

    return answer