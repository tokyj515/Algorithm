

import sys
input = sys.stdin.readline


A = input().rstrip()
B = input().rstrip()


n, m = len(A), len(B)

dp = [[0 for _ in range(m+1)] for _ in range(n+1)]


for i in range(1, n+1):
    for j in range(1, m+1):
        if A[i-1] == B[j-1]:
            dp[i][j] = dp[i-1][j-1]+1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])


max_val = dp[n][m]
print(max_val)

if max_val == 0:
    exit()


i, j = len(A), len(B)
answer = []

while i > 0 and j > 0:
    if A[i-1] == B[j-1]:
        answer.append(A[i-1])
        i -= 1
        j -= 1
    elif dp[i-1][j] == dp[i][j]:
        i -= 1
    else:
        j -= 1


print(''.join(reversed(answer)))




