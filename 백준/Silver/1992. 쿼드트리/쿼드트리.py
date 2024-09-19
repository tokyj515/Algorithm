import sys
input = sys.stdin.readline

n = int(input())

graph = []


for _ in range(n):
    # temp = list(map(int, input())
    temp =  list(map(int, list(input().rstrip())))
    graph.append(temp)


result = ""


def all_same(x, y, size):
    standard = graph[x][y]

    for i in range(x, x+size):
        for j in range(y, y+size):
            if graph[i][j] != standard:
                return False
    return True



def div_and_conq(x, y, size):
    global result

    # 현재 영역이 모두 동일
    if all_same(x, y, size):
        result += str(graph[x][y])
        return



    result += "("
    size //= 2
    div_and_conq(x, y, size)
    div_and_conq(x, y + size, size)
    div_and_conq(x + size, y, size)
    div_and_conq(x+size, y+size, size)
    result += ")"

    # for i in range(x, x+size):
    #     for j in range(y, y+size):
    #         div_and_conq(i, j, )


div_and_conq(0, 0, n)

print(result)