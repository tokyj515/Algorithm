def solution(n):

    n_ones = bin(n).count('1')

    while True:
        n += 1
        if bin(n).count('1') == n_ones:
            return n
