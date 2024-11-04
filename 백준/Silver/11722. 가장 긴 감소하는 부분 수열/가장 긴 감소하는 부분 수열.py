import sys
input = sys.stdin.readline


N = int(input())
num = list(map(int, input().split(" ")))

dp = [1 for _ in range(N+1)]
# dp[0] = 1

for i in range(1, N):
    for j in range(i):
        if num[j] > num[i]:
            dp[i] = max(dp[j] + 1, dp[i])


print(max(dp))