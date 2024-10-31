import sys
input = sys.stdin.readline

N = int(input())

arr =[0 for _ in range(N+1)] # 해당 열의 퀸이 위치간 열 번호 넣기
visited = [0 for _ in range(N+1)] # 해당 열에 퀸이 놓였는지 여부

cnt = 0


def is_possible(row):

    for i in range(row):
        # 같은 열 or 대각선
        if arr[i] == arr[row] or abs(arr[row] - arr[i]) == abs(row - i):
            return False

    return True



def backtrack(row):
    global cnt

    if row == N:
        cnt += 1
        return


    for j in range(N):

        if visited[j]:
            continue

        arr[row] = j

        if is_possible(row):
            visited[j] = 1
            backtrack(row+1)
            visited[j] = 0


backtrack(0)

print(cnt)