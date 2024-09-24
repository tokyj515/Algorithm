import sys
input = sys.stdin.readline


n, k = map(int, input().split(" "))
num = list(map(int, input().split(" ")))



counter = [0 for _ in range(max(num)+1)]

max_val = 0

start = 0
end = 0

while end < n:
    counter[num[end]] += 1
    # counter[end] += 1


    while counter[num[end]] > k:
        counter[num[start]] -= 1
        start += 1
    # while counter[end] > k:
    #     counter[start] -= 1
    #     start += 1


    max_val = max(max_val, end - start + 1)
    # print(counter, max_val, start, end)

    end += 1

print(max_val)