import sys
input = sys.stdin.readline
from collections import deque


n = int(input())
arr = (list(map(int, input().split(" "))) + [0, 0])[:3]


attacks = [
    (9, 3, 1), (9, 1, 3),
    (3, 9, 1), (3, 1, 9),
    (1, 9, 3), (1, 3, 9)
]


queue = deque()
visited = set()

queue.append((arr[0], arr[1], arr[2], 0))
visited.add((arr[0], arr[1], arr[2]))

while queue:
    hp1, hp2, hp3, cnt = queue.popleft()

    if hp1 <= 0 and hp2 <=0 and hp3<=0:
        print(cnt)
        exit()


    for a in attacks:
        new1 = max(0, hp1 - a[0])
        new2 = max(0, hp2 - a[1])
        new3 = max(0, hp3 - a[2])

        if (new1, new2, new3) not in visited:
            visited.add((new1, new2, new3))
            queue.append((new1, new2, new3, cnt+1))


print(-1)



