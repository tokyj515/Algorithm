import copy

def solution(begin, target, words):
    result = 10000
    visited = [0 for _ in range(len(words))]

    answer = []
    res = []

    def can_change(now, word):
        differ = 0
        j = 0


        while j < len(now):
            if word[j] != now[j]:
                differ += 1

            j += 1
        # print(f"now: {now},  word: {word} => {differ}")
            
        if differ == 1:
            return True
        else:
            return False




    def backtrack(dep, now):

        nonlocal result

        if target not in words:
            result = 0
            return


        if now == target:
            result = min(result, dep)

#             temp = copy.deepcopy(answer)
#             res.append(temp)

#             print(now, target, dep, result, temp)
            return

        for i, word in enumerate(words):
            if can_change(now, word) and not visited[i]:
                answer.append(word)
                visited[i] = 1
                backtrack(dep + 1, word)
                visited[i] = 0
                answer.pop()




    # can_change("hit")


    backtrack(0, begin)
    
    return result