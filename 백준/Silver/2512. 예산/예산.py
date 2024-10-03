import sys
input = sys.stdin.readline


n = int(input())

arr = list(map(int, input().split(" ")))

total = int(input())

min_val = min(arr)
max_val = max(arr)

def binary_search():
    left = 0
    right = max(arr)
    result = 0


    while left <= right:
        mid = (left+right) // 2

        budget = 0
        for a in arr:
            if a <= mid:
                budget += a
            else:
                budget += mid


        if budget <= total:
            result = mid
            left = mid + 1
        else:
            right = mid - 1

        # print(result)

    return result






result = binary_search()

print(result)