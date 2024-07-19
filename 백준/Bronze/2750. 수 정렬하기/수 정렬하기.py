N = int(input())
num = []

for i in range(N):
    num.append(int(input()))

num.sort(reverse=False)

for n in num:
    print(n)