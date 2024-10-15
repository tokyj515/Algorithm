cnt = 0

N = int(input())
num = list(map(int, input().split(" ")))

num.sort()


cnt = 0

for i in range(N):
    target = num[i]

    left = 0
    right = N-1



    while left < right:

        if left == i:
            left += 1
            continue

        if right == i:
            right -= 1
            continue


        total = num[left] + num[right]


        if total == target:
            cnt += 1
            break
        elif total < target:
            left += 1
        else:
            right -= 1

print(cnt)