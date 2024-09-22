import sys
from collections import Counter
input = sys.stdin.readline


n, d, k, c = map(int, input().split(" "))


# 벨트
belt = []
for _ in range(n):
    temp = int(input())
    belt.append(temp)


# k개의 초밥을 선택했을 때 어떤 초밥 종류가 있는지
count = [0 for _ in range(d+1)]
type = 0

# 초기 세팅 1번 초밥부터 k초밥까지
for i in range(k):
    if count[belt[i]] == 0:
        type += 1
    count[belt[i]] += 1


max_type = type

if count[c] == 0:
    max_type += 1


for i in range(1, n):

    # 왼쪽 초밥 빼기
    temp = belt[i-1]
    count[temp] -= 1

    if count[temp] == 0:
        type -= 1


    # 새로운 초밥 추가
    new = belt[(i+k-1) % n]
    if count[new] == 0:
        type += 1
    count[new] += 1

    coupon = 0
    if count[c] == 0:
        coupon = 1

    max_type = max(max_type, type + coupon)

    # print(count, max_type)



print(max_type)