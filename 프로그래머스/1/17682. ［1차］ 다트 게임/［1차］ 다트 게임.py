def solution(dartResult):
    dartResult = list(dartResult)



    dart = []
    answer = []

    # 숫자와 문자 분리
    temp = ''
    for i in range(len(dartResult)):
        if dartResult[i].isdigit():
            temp += dartResult[i]
        else:
            if temp:
                dart.append(temp)
            dart.append(dartResult[i])
            temp = ''

    # print(dart)

    for i in range(len(dart)):
        num = 0
        bonus = ''

        if dart[i].isdigit():


            # 제곱 세팅
            num = int(dart[i])
            bonus = dart[i + 1]

            # 더하기
            if bonus == 'S':
                answer.append(pow(num, 1))
            elif bonus == 'D':
                answer.append(pow(num, 2))
            elif bonus == 'T':
                answer.append(pow(num, 3))

            # 옵션
            option = ''
            if i + 2 < len(dart) and not dart[i + 2].isdigit():
                option = dart[i + 2]

                if option == '*':
                    if len(answer) == 1:
                        last = int(answer.pop())
                        last *= 2
                        answer.append(last)

                    elif len(answer) == 2 or len(answer) == 3:
                        last = int(answer.pop())
                        last *= 2
                        lastBefore = int(answer.pop())
                        lastBefore *= 2

                        answer.append(lastBefore)
                        answer.append(last)

                elif option == '#':
                    last = int(answer.pop())
                    last *= -1
                    answer.append(last)

        else:
            continue

    return sum(answer)
