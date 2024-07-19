import sys


input = sys.stdin.readline


# 그래프
n, m = map(int, input().split())
graph = []

graph.append([0 for _ in range(m+1)])

for _ in range(n):
    temp = list(map(int, input().split()))
    graph.append([0] + temp)





sum = [[0 for _ in range(m+1)] for _ in range(n+1)]
# sum[1][1] = graph[1][1]


for i in range(1, n+1):
    for j in range(1, m+1):
        sum[i][j] = graph[i][j] + sum[i-1][j] + sum[i][j-1] - sum[i-1][j-1] 


# print("그래프")
# for row in graph:
#     print(row)

# print()
# print("합")
# for row in sum:
#     print(row)

# print()

tc = int(input())

for _ in range(tc):
    x1, y1, x2, y2 = map(int, input().split())
    # total = sum[x2][y2] - sum[x1][y2-y1] - sum[x2-x1][y1] + sum[x2-x1][y2-y1]
    total = 0
    if x1 ==1 and y1==1:
        total = sum[x2][y2]
    else:
        garo = x2 - x1
        sero = y2 - y1
        # total = sum[x2][y2] - sum[x2][y1-garo] - sum[x1-sero][y2] + sum[x1-sero][y1-garo]
        # sum[3][3] - sum[3, 1] - sum[1][3] + sum[1][1]
        total = sum[x2][y2] - sum[x2][y1-1] - sum[x1-1][y2] + sum[x1-1][y1-1]
    print(total)

 









# 테스트케이스

