import sys

input = sys.stdin.readline


k = int(input())


num = []
for i in range(k):
    n = int(input())
    num.append([i+1, n])

num.sort(reverse=True)


# print(num)

cnt = 0

for i in range(k-1):
    a = num[i]
    b = num[i+1]

    if a[1] <= b[1]:
        cnt += b[1] - (a[1]- 1) 
        b[1] = a[1]- 1
    
    # print(num)
    # print(cnt)
       
print(cnt)
       