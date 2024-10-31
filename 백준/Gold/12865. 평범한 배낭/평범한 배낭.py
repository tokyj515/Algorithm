
import sys
input = sys.stdin.readline

N, K = map(int, input().split(" "))

bag = []
for _ in range(N):
    w, v = map(int, input().split(" "))
    bag.append((w, v))

bag.sort()

dp = [0 for _ in range(K+1)]





for i in range(len(bag)):
    w, v = bag[i]

    for j in range(K, w-1, -1):
        dp[j] = max(dp[j], dp[j-w]+v)

print(dp[K])


