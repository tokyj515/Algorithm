from collections import defaultdict

def solution(tickets):
    graph = defaultdict(list)
    
    # 그래프 생성 및 정렬 (사전순 보장)
    for a, b in tickets:
        graph[a].append(b)
    for key in graph:
        graph[key].sort()
    
    answer = ["ICN"]  # 시작점
    result = []  # 결과 경로를 저장

    def dfs(v):
        # 모든 티켓을 사용한 경우
        if len(answer) == len(tickets) + 1:
            result.append(answer[:])  # 현재 경로를 복사해 저장
            return True  # 경로를 찾았으므로 더 이상 탐색하지 않음

        for i, next_dest in enumerate(graph[v]):
            graph[v].pop(i)  # 티켓 사용
            answer.append(next_dest)
            if dfs(next_dest):  # 경로를 찾으면 바로 종료
                return True
            answer.pop()  # 백트래킹
            graph[v].insert(i, next_dest)  # 티켓 복구

        return False  # 현재 노드에서 경로를 찾지 못함

    dfs("ICN")
    return result[0]  # 사전순으로 가장 앞선 경로 반환
