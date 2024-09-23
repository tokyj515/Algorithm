# 기둥 개수 입력
N = int(input())

# 기둥의 위치와 높이를 저장할 리스트
pillars = []

# 입력받은 기둥 정보를 저장
for _ in range(N):
    L, H = map(int, input().split())
    pillars.append((L, H))

# 기둥을 위치(L) 기준으로 정렬
pillars.sort()

# 가장 높은 기둥을 찾기
max_height = 0
max_index = 0
for i in range(N):
    if pillars[i][1] > max_height:
        max_height = pillars[i][1]
        max_index = i

# 면적 계산
area = 0

# 왼쪽에서부터 가장 높은 기둥까지 면적 계산
left_max = pillars[0][1]
for i in range(max_index):
    if pillars[i][1] > left_max:
        left_max = pillars[i][1]
    area += left_max * (pillars[i + 1][0] - pillars[i][0])

# 오른쪽에서부터 가장 높은 기둥까지 면적 계산
right_max = pillars[-1][1]
for i in range(N - 1, max_index, -1):
    if pillars[i][1] > right_max:
        right_max = pillars[i][1]
    area += right_max * (pillars[i][0] - pillars[i - 1][0])

# 가장 높은 기둥의 면적 더하기
area += max_height

# 결과 출력
print(area)
