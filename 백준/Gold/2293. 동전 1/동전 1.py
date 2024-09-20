import sys
input = sys.stdin.readline


n, k = map(int, input().split(" "))

num = []
dp = [0 for _ in range(k+1)]

for _ in range(n):
    temp = int(input())
    num.append(temp)

dp[0] = 1

for n in num:
    for i in range(n, k+1):
        dp[i] += dp[i-n]
    # print(dp)


print(dp[k])