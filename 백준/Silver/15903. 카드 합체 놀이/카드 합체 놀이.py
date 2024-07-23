import sys
import heapq

input = sys.stdin.readline

n, k = map(int, input().split(" "))

num = list(map(int, input().split(" ")))

heapq.heapify(num)

# print(num)


for _ in range(k):
    a, b = heapq.heappop(num), heapq.heappop(num)

    heapq.heappush(num, a+b)
    heapq.heappush(num, a+b)

    # print(num)


print(sum(num))