# import sys
# sys.stdin = open("input.txt", "r")

L, C = map(int, input().split())
arr = input().split()
arr.sort()  # 사전순 정렬

answer = []
result = []

# 모음과 자음 조건 확인
def check(temp):
    mo = 0  # 모음 개수
    ja = 0  # 자음 개수

    for t in temp:
        if t in ('a', 'e', 'i', 'o', 'u'):
            mo += 1
        else:
            ja += 1

    return mo >= 1 and ja >= 2  # 최소 모음 1개, 자음 2개 조건

# 백트래킹 함수
def backtrack(dep, pre):
    if dep == L:  # 길이가 L인 암호 완성
        if check(answer):  # 조건에 맞는 경우만 결과에 추가
            result.append("".join(answer))
        return

    for i in range(pre, C):
        answer.append(arr[i])
        backtrack(dep + 1, i + 1)
        answer.pop()

# 백트래킹 시작
backtrack(0, 0)

# 결과 출력
for res in result:
    print(res)
