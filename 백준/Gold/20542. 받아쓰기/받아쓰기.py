import sys
input = sys.stdin.readline

n, m = map(int, input().split())
write = input().rstrip()
correct = input().rstrip()

def i_check(a, b):
    return (a == 'i' and b in ['i', 'j', 'l'])

def v_check(a, b):
    return (a == 'v' and b in ['v', 'w'])

dp = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(n + 1):
    dp[i][0] = i

for j in range(m + 1):
    dp[0][j] = j

for i in range(1, n + 1):
    for j in range(1, m + 1):
        if write[i-1] == correct[j-1]:
            dp[i][j] = dp[i-1][j-1]
        else:
            dp[i][j] = min(
                dp[i-1][j] + 1,    # Deletion
                dp[i][j-1] + 1,    # Insertion
                dp[i-1][j-1] + 1   # Replacement
            )
            if i_check(write[i-1], correct[j-1]) or v_check(write[i-1], correct[j-1]):
                dp[i][j] = min(dp[i][j], dp[i-1][j-1])

print(dp[n][m])