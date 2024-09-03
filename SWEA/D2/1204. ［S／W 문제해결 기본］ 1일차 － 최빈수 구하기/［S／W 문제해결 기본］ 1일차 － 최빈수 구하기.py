from collections import Counter

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    test_case = int(input())
    
    num = list(map(int, input().split()))

    counter = Counter(num)

    sorted_counter = sorted(counter.items(), key=lambda item: (-item[1], -item[0]))

    #print(sorted_counter)   
    
    print(f"#{test_case} {sorted_counter[0][0]}")