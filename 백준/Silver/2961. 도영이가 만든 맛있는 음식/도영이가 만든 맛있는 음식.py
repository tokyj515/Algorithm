import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


# 재료 n개
# S신 곱
# B쓴 합

n = int(input())
foods = []
visited = [0 for _ in range(n)]

for _ in range(n):
    s, b = map(int, input().split(" "))
    foods.append([s, b])


answer = []
min_val = 1000000000


def mul(arr):
    result = 1

    for a in arr:
        result *= a
    return result


def backtrack(dep, max_dep, pre):
    global min_val
    # temp = answer[::]
    # sour = [x[0] for x in temp]
    # bitter = [x[1] for x in temp]

    # if abs(sum(sour)-sum(bitter)) < min_val:

    if dep == max_dep:
        temp = answer[::]
        sour = [x[0] for x in temp]
        bitter = [x[1] for x in temp]

        # print(temp)

        if abs(mul(sour) - sum(bitter)) < min_val:
            min_val = abs(mul(sour) - sum(bitter))
            # print(mul(sour), sum(bitter), min_val)
            # print()
        return


    for i in range(pre, n):
        if not visited[i]:
            answer.append(foods[i])
            visited[i] = 1
            backtrack(dep + 1, max_dep, i+1)
            answer.pop()
            visited[i] = 0





for i in range(1, n+1):
    backtrack(0, i, 0)


print(min_val)