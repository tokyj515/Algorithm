import sys

n, target = map(int, sys.stdin.readline().split(" "))
tree = list(map(int, sys.stdin.readline().split(" ")))

start = 1
end = max(tree)


while start <= end:
    # 선택된 높이
    mid = (start + end) // 2
    differ = 0

    # 선택된 높이에서 자르면 남는 나무
    for t in tree:
        if t > mid:
            differ += (t - mid)

    # start와 end 조정 -> mid값을 조정하기 위해
    if differ >= target:
        start = mid + 1
    else:
        end = mid - 1


print(end)