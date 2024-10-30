

import sys
input = sys.stdin.readline

n, k = map(int, input().split(" "))
money = []
for _ in range(n):
    temp = int(input())
    money.append(temp)

dp = [0 for _ in range(k+1)]
dp[0] = 1


for coin in money:

    for i in range(coin, k+1):
        dp[i] += dp[i-coin]


print(dp[k])