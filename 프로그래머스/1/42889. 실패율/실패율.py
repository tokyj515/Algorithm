from collections import Counter


def solution(N, stages):
    # N: 전체 스테이지 수 -> 배열 크기
    # stages: 사용자가 멈춰있는 스테이지 번호 -> Counter
    # challenger: 참여인원
    # counter: 각 단계에 머물러 있는 인원 수 (오름차순)


    #
    percent = []
    result = []


    # 변수 선언
    people = len(stages)
    counter = Counter(stages)
    counter = sorted(counter.items())

    counter_list = []
    num = [x for x in range(N+1)]
    round  = [x[0] for x in counter]

    for n in num:
        if n not in round:
            counter_list.append((n, 0))
    for c in counter:
        counter_list.append(c)

    counter_list.sort(key=lambda x : x[0])
    counter_list.pop(0)




    for count in counter_list:

        if people != 0:
            percent.append((count[0], count[1] / people))
        else:
            percent.append((count[0], 0.0))

        people -= count[1]

    if len(percent) == N + 1:
        percent.pop()

    percent.sort(key=lambda x: -x[1])

    for p in percent:
        result.append(p[0])

    return result
