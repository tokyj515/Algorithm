

import sys
input = sys.stdin.readline


s = input().rstrip()

stick = 0
answer = 0


for i in range(len(s)):

    if s[i] == "(":
        stick += 1
    else:
        stick -= 1

        if s[i-1] == '(':
            answer += stick
        else:
            answer += 1

print(answer)