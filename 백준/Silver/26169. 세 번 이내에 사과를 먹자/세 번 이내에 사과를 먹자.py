import copy
import sys
input = sys.stdin.readline


graph = []
for _ in range(5):
    temp = list(map(int, input().rstrip().split(" ")))
    graph.append(temp)

origin = copy.deepcopy(graph)

r, c = map(int, input().split(" "))


# 좌측 상단 -> 우측 하단
# dx = [0, 0, 1, -1]
# dy = [1, -1, 0, 0]

dx = [-1, 0, 0, 1]
dy = [0, 1, -1, 0]

idx = 0

answer = []
result = []

def possible(answer):
    root = []

    for i, j in answer:
        root.append(origin[i][j])

    # print(f"{answer}: {root}")
    # 시작점이 r, c인지
    # 길이가 2 이상인지
    # 1이 2개 이상 들어있는지
    if answer[0] == [r, c] and len(answer) >= 2 and root.count(1) >= 2:
        # print(f"{answer}: {root}")
        return True
    return False



def backtrack(dep, r, c):
    global idx

    if dep == 4:
        temp = answer[::]
        # print(temp)
        # print(temp, possible(temp), temp not in result)
        if possible(temp) and temp not in result:
            result.append(temp)
            # print(result)
        # else:
        #     result.append(temp)
        return

    if 0<= r and r <5 and 0<=c and c<5 and graph[r][c] != -1:
        temp = origin[r][c]

        graph[r][c] = -1
        answer.append([r, c])
        
        for i in range(4):
            nx = r + dx[i]
            ny = c + dy[i]
            backtrack(dep+1, nx, ny)
        # 
        # backtrack(dep + 1, r-1, c)
        # backtrack(dep + 1, r, c+1)
        # backtrack(dep + 1, r, c-1)
        # backtrack(dep + 1, r+1, c)

        # for i in range(4):
        #     nx = r + dx[i]
        #     ny = c + dy[i]
        #
        #     if 0 <= nx and nx <5 and 0<= ny and ny <5:
        #         idx += 1
        #         print(f"idx: {idx}, {r, c}")
        #         backtrack(dep+1, nx, ny)
        #
        #     # graph[nx][ny] = origin[nx][ny]
        #     # answer.pop()

        graph[r][c] = origin[r][c]
        answer.pop()




backtrack(0, r, c)

# print(result)



if result:
    print(1)
else:
    print(0)
