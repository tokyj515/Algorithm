import sys
input = sys.stdin.readline

cnt = 0

n, m = map(int, input().split())

known = list(map(int, input().split()))[1:]
# print(f"known: {known}")

# graph = [[0 for _ in range(n+1)] for _ in range(n+1)]
graph = [[] for _ in range(n+1)]
visited = [0 for _ in range(n+1)]


party = []


def dfs(v):
    visited[v] = 1
    # print(v, end=" ")


    for i in graph[v]:
        if not visited[i]:
            dfs(i)





for _ in range(m):
    people = list(map(int, input().split()))[1:]
    # print(f"people: {people}")

    party.append(people)

    if len(people) == 1:
        continue

    # 그래프 세팅
    for i in range(0, len(people)):
        for j in range(0, len(people)):
            if i == j:
                continue
            graph[people[i]].append(people[j])
            graph[people[j]].append(people[i])

# print("graph:")
for row in graph:
    row = list(set(row))
    # print(row)



# dfs
# print("dfs:")
for i in known:
    if not visited[i]:
        dfs(i)
        # print()

# print(visited)



# 몇개의 파티에 갈 수 있는지
for p in party:

    flag = True

    for e in p:
        if visited[e]:
            flag = False

    if flag:
        cnt += 1

print(cnt)