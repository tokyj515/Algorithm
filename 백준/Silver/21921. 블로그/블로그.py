import sys
input = sys.stdin.readline


n, x = map(int, input().split(" "))

arr = list(map(int, input().split(" ")))
prefix = [0 for _ in range(n)]
prefix[0] = arr[0]

max_val = 0
cnt = 0

for i in range(1, n):
    prefix[i] = prefix[i-1] + arr[i]

prefix = [0] +prefix


for i in range(n, -1, -1):
    hap = prefix[i] - prefix[i-x]

    if hap > max_val:
        max_val = hap
        cnt = 1
    elif hap == max_val:
        cnt += 1


# # i: 기준점
# for i in range(n-x+1):
#     hap = sum(arr[i:i+x])
#
#     if hap > max_val:
#         max_val = hap
#         cnt = 1
#     elif hap == max_val:
#         cnt += 1
#
#         # print(arr[i:i+x])
#         # print(f"hap: {hap}, max_val:{max_val}, cnt: {cnt}")
#         # print()
#



if max_val == 0:
    print("SAD")
else:
    print(max_val)
    print(cnt)