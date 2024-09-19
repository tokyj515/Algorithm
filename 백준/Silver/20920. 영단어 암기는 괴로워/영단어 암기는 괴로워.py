import sys
from collections import Counter
input = sys.stdin.readline

n, m = map(int, input().split(" "))

word = []


for _ in range(n):
    temp = input().rstrip()

    if len(temp) >= m:
        word.append(temp)


counter = dict(Counter(word))

sorted_counter  = sorted(counter.items(), key=lambda x:(-x[1], -len(x[0]), x[0]))

for word in sorted_counter:
    print(word[0])

