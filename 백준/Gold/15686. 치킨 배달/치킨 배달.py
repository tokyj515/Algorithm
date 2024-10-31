import sys
input = sys.stdin.readline


N, M = map(int, input().split(" "))

graph = []
for _ in range(N):
    temp = list(map(int, input().split(" ")))
    graph.append(temp)

# 치킨 거리(맨허튼 거리): 집에서 가장 가까운 치킨집과의 거리
# 0은 빈 칸 | 1은 집 | 2는 치킨집

store = []
house = []

for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            house.append((i, j))
        elif graph[i][j] == 2:
            store.append((i, j))


# 살릴 집 조합
combi_list = []
visited = [0 for _ in range(len(store))]
answer = []

def backtrack(dep, pre):

    if dep == M:
        temp = answer[::]
        combi_list.append(temp)
        return


    for i in range(pre, len(store)):
        if not visited[i]:
            answer.append(store[i])
            visited[i] = 1
            backtrack(dep + 1, i+1)
            answer.pop()
            visited[i] = 0


backtrack(0, 0)


min_val = 1e9

for spot in combi_list:

    dist = 0

    # 집에서 가장 가까운 치킨집 찾기
    for hx, hy in house:
        min_dist = 1e9

        for cx, cy in spot:
            min_dist = min(min_dist, abs(hx-cx)+abs(hy-cy))

        dist += min_dist



    # print(f"spot: {spot} => {dist}")

    min_val = min(min_val, dist)


print(min_val)


