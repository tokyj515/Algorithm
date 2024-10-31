import sys
input = sys.stdin.readline

graph = []
for _ in range(9):
    temp = list(map(int, list(input().rstrip())))
    graph.append(temp)

coor = []

for i in range(9):
    for j in range(9):
        if graph[i][j] == 0:
            coor.append((i, j))



def is_possible(x, y, num):

    for i in range(9):
        if graph[i][y] == num:
            return False


    for j in range(9):
        if graph[x][j] == num:
            return False


    start_x = (x//3) *3
    start_y = (y//3)*3
    for i in range(3):
        for j in range(3):
            if graph[start_x+ i][start_y + j]  == num:
                return False

    return True





def backtrack(idx):


    if idx == len(coor):
        temp = [row[::] for row in graph]
        for row in temp:
            print("".join(map(str, row)))
        exit()

    x, y = coor[idx]

    for num in range(1, 10):
        if is_possible(x, y, num):
            graph[x][y] = num
            backtrack(idx+1)
            graph[x][y] = 0



backtrack(0)