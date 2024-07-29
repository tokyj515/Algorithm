def solution(n):
    dp = [0 for _ in range(n+1)]
    
    # 인덱스 -> 가로 바닥의 길이
    
    dp[0] = 0
    dp[1] = 1
    dp[2] = 2
    
    for i in range(3, n+1):
        dp[i] = (dp[i-2] + dp[i-1]) % 1000000007
        
    return dp[n]