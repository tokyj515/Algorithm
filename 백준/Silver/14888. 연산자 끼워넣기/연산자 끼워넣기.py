import sys
input = sys.stdin.readline



# 변수
N = int(input())
num = list(map(int, input().split(" ")))

temp = list(map(int, input().split(" ")))

op = []
for i in range(4):
    for t in range(temp[i]):
        op.append(i)

max_val = -float('inf')
min_val = float('inf')


# 연산자 순열
permu_list = []
answer = []
visited = [0 for _ in range(len(op))]

def backtrack(dep):

    if dep == len(op):
        temp = answer[::]
        permu_list.append(temp)
        return


    for i in range(len(op)):
        if not visited[i]:
            answer.append(op[i])
            visited[i] = 1

            backtrack(dep+1)

            answer.pop()
            visited[i] = 0

backtrack(0)





for arr in permu_list:
    res = num[0]

    for i in range(len(arr)):
        a = arr[i]
        y = num[i+1]

        if a == 0:  # 더하기
            res = res + y

        elif a == 1:    # 뺄셈
            res = res - y

        elif a == 2:    # 곱셈
            res = res * y

        else:   # 나눗셈
            if res < 0:
                res = -(abs(res) // y)
            else:
                res = res // y

    # print(f"arr: {arr} => {res}")
    max_val = max(max_val, res)
    min_val = min(min_val, res)


print(max_val)
print(min_val)
