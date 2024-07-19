import sys
import copy

input = sys.stdin.readline

# 로또를 num에서 6개 뽑을 것 -> 서로 다른 숫자를 중복 없이 6개 -> 조합문제



while True:
    num = list(map(int, input().split(" ")))

    n = num[0]
    num = num[1:]

    if n == 0:
        break


    visited = [0 for _ in range(n+1)] # num리스트의 개수만큼
    arr = [0 for _ in range(6)] # -> 6개 담을 것
    answer = []



    def func(num, dep, pre):
        # 뽑을 개수 dep
        if dep == 6:
            temp = copy.deepcopy(arr)
            answer.append(temp)
            # print("dep: ", dep, " arr: ", arr)
            return

        for i in range(pre, len(num)):
            # 이전 인덱스부터 시작해야 뒷 부분에서의 순열을 구할 수 있음
            if visited[i] == 0:
                # 현재 뎁스(k)에 i번째 num 넣기
                arr[dep] = num[i]

                visited[i] = 1
                func(num, dep + 1, i)
                visited[i] = 0


    func(num, 0, 0)


    for a in answer:
        a = [str(i) for i in a]
        print(' '.join(a))
    print()