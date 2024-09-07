n = int(input())

for i in range(1, n + 1):
    num = str(i)  # i를 문자열로 변환
    cnt = 0

    # '3', '6', '9'의 등장 횟수를 카운트
    cnt += num.count('3')
    cnt += num.count('6')
    cnt += num.count('9')

    if cnt == 0:
        print(i, end=" ")  # 숫자를 출력
    else:
        print('-' * cnt, end=" ")  # '-'를 cnt만큼 출력
