import sys
input = sys.stdin.readline

n, k = map(int, input().split(" "))
money = []
for _ in range(n):
    temp = int(input())
    money.append(temp)

dp = [float('inf') for _ in range(k+1)]
dp[0] = 0


for coin in money:
    for i in range(coin, k+1):
        dp[i] = min(dp[i], dp[i-coin]+1)


if dp[k] == float('inf'):
    print(-1)
else:
    print(dp[k])