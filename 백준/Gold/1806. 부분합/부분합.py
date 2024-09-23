import sys
from collections import Counter
input = sys.stdin.readline


n, s = map(int, input().split(" "))

num = list(map(int, input().split(" ")))


sum = num[0]
start = 0
end = 0

min_val = 100000000000

while True:
    if sum >= s:
        min_val = min(min_val, end-start+1)
        sum -= num[start]
        start += 1
    else:
        end +=1
        if end == n:
            break
        sum += num[end]

if min_val == 100000000000:
    print(0)
else:
    print(min_val)