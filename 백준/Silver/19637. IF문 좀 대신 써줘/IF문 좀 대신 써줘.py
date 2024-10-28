
from bisect import bisect_left, bisect_right
import sys
input = sys.stdin.readline

N, M = map(int, input().split(' '))

standard = []
for _ in range(N):
    name, limit = input().split()
    limit = int(limit)

    if not standard or standard[-1][0] != limit:
        standard.append([limit, name])


for _ in range(M):
    target = int(input())


    left, right = 0, len(standard)

    while left < right:
        mid = (left+right) //2

        if standard[mid][0] < target:
            left = mid + 1
        else:
            right = mid

    print(standard[left][1])



