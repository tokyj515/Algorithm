import sys
input = sys.stdin.readline


N, M = map(int, input().split(" "))


keywords = set()

for _ in range(N):
    temp = input().rstrip()
    keywords.add(temp)


for _ in range(M):
    memos = set(input().rstrip().split(","))
    keywords -= memos
    print(len(keywords))
