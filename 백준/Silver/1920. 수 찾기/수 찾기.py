import sys



# 반복문



n = sys.stdin.readline()
data = list(map(int, sys.stdin.readline().split(" ")))
m = sys.stdin.readline()
find_data = list(map(int, sys.stdin.readline().split(" ")))

data.sort()
# find_data.sort()


def binary_search(target, data):
    start = 0
    end = len(data) - 1

    while start <= end:
        mid = (start + end) // 2

        if data[mid] == target:
            return 1
        elif data[mid] < target:
            start = mid + 1
        else:
            end = mid - 1

    return 0


for t in find_data:
    print(binary_search(t, data))

