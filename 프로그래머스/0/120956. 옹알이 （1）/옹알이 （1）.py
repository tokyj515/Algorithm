def solution(babbling):
    answer = 0

    word = ["aya", "ye", "woo", "ma"]

    for i in range(0, len(babbling)):
        for w in word:
            if w in babbling[i]:
                babbling[i] = babbling[i].replace(w, '*')

    # for b in babbling:
    #     for w in word:
    #         for i in range(0, b.count(w)):
    #             b = b.replace(w, '')

    for element in babbling:
        if all(e == "*" for e in element):
            answer += 1

    return answer
