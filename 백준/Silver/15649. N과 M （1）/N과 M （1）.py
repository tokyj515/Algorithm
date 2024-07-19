import sys
import copy

input = sys.stdin.readline

answer = []
n, k = map(int, input().split(" "))

visited = [0 for _ in range(n+1)]

arr = [0 for _ in range(k)]



# 2차
def dfs(dep):
    if dep == k:
        # answer.append(arr) -> 전역 변수라서 매 경우의 수가 같이 공유하고 있음 -> 최종 데이터로 바뀌어 버림!
        # print("dep: ", dep, " arr: ", arr)
        temp = copy.deepcopy(arr)
        answer.append(temp)
        return

    for i in range(1, n+1):
        if visited[i] == 0:
            arr[dep] = i

            visited[i] = 1
            dfs(dep+1)
            visited[i] = 0

dfs(0)

for a in answer:
    print(' '.join(list(map(str, a))))
