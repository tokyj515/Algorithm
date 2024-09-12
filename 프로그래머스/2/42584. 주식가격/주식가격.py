def solution(prices):
    n = len(prices)
    answer = [0 for _ in range(n)]
    
    stack = []

    for i in range(n):
        
        while stack and prices[i] < prices[stack[-1]]:
            
            now = stack.pop()
            answer[now] = i - now
        
        stack.append(i)
        
        # print(f"answer: {answer}")
        
    
    while stack:
        now = stack.pop()
        answer[now] = n - now -1
        
    return answer
    