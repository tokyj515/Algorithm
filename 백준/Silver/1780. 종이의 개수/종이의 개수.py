import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)  # 재귀 깊이 제한을 100만으로 늘리기

n = int(input())

graph = []
for _ in range(n):
    temp = list(map(int, input().rstrip().split(" ")))
    graph.append(temp)

# for row in graph:
#     print(row)


# -1로만, 0으로만, 1로만
result = [0, 0, 0]

def check(x, y, n):
    standard = graph[x][y]

    for i in range(x, x+n):
        for j in range(y, y+n):
            if graph[i][j] != standard:
                return False
    return True



def count(x, y, n):

    standard = graph[x][y]

    if check(x, y, n):
        result[standard+1] += 1
        return

    nn = n // 3
    for i in range(3):
        for j in range(3):
            count(x + i*nn, y +j*nn, nn)





count(0, 0, n)




for res in result:
    print(res)

