import sys
input = sys.stdin.readline

# n: 한 변 길이
# m개의 파이어볼
# 한 파이어볼이 이동 후 이동한 점에 2개 이상의 파이어볼이 있으면
#  -> 파이어볼을 모두 합침
#  -> 4개로 나눔


n, m, k = map(int, input().split(" "))

graph = [[[] for _ in range(n)] for _ in range(n)]

# r, c에 m(값), d(방향), s(속력).
# d 방향으로 s만큼 이동
# n-1행, 열에서 0번으로 연결

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]


for _ in range(m):
    r, c, m, s, d = map(int, input().split(" "))
    # graph[r-1][c-1].pop()
    graph[r-1][c-1].append([m, d, s])
    # graph[r-1][c-1] = [m, d, s]

# for row in graph:
#     print(row)
# print()



for _ in range(k):

    move = []
    new_graph = [[[] for _ in range(n)] for _ in range(n)]

    # 이동 위치할 위치 찾기
    for i in range(n):
        for j in range(n):

            if graph[i][j]:
                while graph[i][j]:
                    temp = graph[i][j].pop(0)
                    m = temp[0]
                    d = temp[1]
                    s = temp[2]

                    nx = (i + dx[d] * s + n) % n
                    ny = (j + dy[d] * s + n) % n

                    # move.append([nx, ny, m, d, s])
                    new_graph[nx][ny].append([m, d, s])

    # 각 단계에서 이동한 거 세팅
    for nx, ny, m, d, s in move:
        graph[nx][ny].append([m, d, s])
    # 
    # for row in graph:
    #     print(row)
    # print()


    # 4개로 분할
    for i in range(n):
        for j in range(n):

            if len(new_graph[i][j]) > 1:
                cnt = len(new_graph[i][j]) # 총 파이어볼 개수

                # 일단 전부 합친 거
                total_m = sum([x[0] for x in new_graph[i][j]])
                total_s = sum([x[2] for x in new_graph[i][j]])

                m = total_m // 5
                s = total_s // cnt

                if m == 0:
                    new_graph[i][j] = []
                    continue


                # 방항 정리하고 파이어볼 심기
                direct = [x[1] for x in new_graph[i][j]]
                odd = 0
                even = 0
                for d in direct:
                    if d % 2 == 1: odd += 1
                    else: even += 1


                if odd == cnt or even == cnt:
                    next_direct = [0, 2, 4, 6]
                else:
                    next_direct = [1, 3, 5, 7]

                new_graph[i][j] = []
                for d in next_direct:
                    new_graph[i][j].append([m, d, s])
    graph = new_graph

    # print("final")
    # for row in graph:
    #     print(row)
    # print()


result = 0

for i in range(n):
    for j in range(n):
        if graph[i][j]:
            cnt = sum([x[0] for x in graph[i][j]])
            result += cnt

print(result)



