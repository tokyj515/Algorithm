def solution(n, times):
    left = 1
    right = max(times) * n  # 최대 시간
    answer = right  # 최악의 경우로 초기화

    while left <= right:
        mid = (left + right) // 2

        # 현재 시간(mid) 동안 처리 가능한 총 사람 수
        total_people = sum(mid // t for t in times)

        if total_people >= n:
            answer = mid  # 현재 시간을 저장 (더 작은 시간 가능성 탐색)
            right = mid - 1
        else:
            left = mid + 1  

    return answer
