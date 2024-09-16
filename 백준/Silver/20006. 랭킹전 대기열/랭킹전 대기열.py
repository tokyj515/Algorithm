import sys
input = sys.stdin.readline


p, m = map(int, input().split(" "))



people = []

for _ in range(p):
    level, nickname = input().rstrip().split(" ")
    level = int(level)
    people.append([level, nickname])

# print(people)

rooms = []
standard = []




for i in range(p):
    now = people[i]
    flag = False

    for j, room in enumerate(rooms):

        # 현재 룸의 레벨이 now랑 맞는지
        if len(room) < m and standard[j] - 10  <= now[0] and now[0] <= standard[j] + 10:
            room.append(now)
            flag = True
            break

    # 안 맞는 경우
    if not flag:
        rooms.append([now])
        standard.append(now[0])



for room in rooms:
    if len(room) == m:
        print("Started!")
    else:
        print("Waiting!")

    room = sorted(room, key=lambda x : x[1])

    for p in room:
        print(*p)

