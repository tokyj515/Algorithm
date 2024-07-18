def solution(friends, gifts):
    answer = 0
    
    gift_map = {} # A->B로 몇개
    giver_map = {} # 준 사람의 횟수
    receiver_map = {} # 받은 사람의 횟수
    answer_map = {} # 다음달에 받을 수


    # 각 정보를 넣을 map을 0으로 초기화 및 세팅하는 작업
    for e1 in friends:
        value_map = {}
        for e2 in friends:
            if e1 == e2: continue
            value_map[e2] = 0
        gift_map[e1] = value_map
        giver_map[e1] = 0
        receiver_map[e1] = 0
        answer_map[e1] = 0
    
    
    #gift 리스트 파싱해서 정보 넣기
    for e in gifts:
        A, B = e.split()
        gift_map[A][B] += 1
        giver_map[A] += 1
        receiver_map[B] += 1
    
    
    # 실제 로직
    for i in range(len(friends) -1):
        for j in range(i+1, len(friends)):
            A = friends[i]
            B = friends[j]
            
            # 기록 존재o
            if gift_map[A][B] > gift_map[B][A]:
                answer_map[A] += 1
            elif gift_map[B][A] > gift_map[A][B]:
                answer_map[B] += 1
            else:
                A_value = giver_map[A] - receiver_map[A]
                B_value = giver_map[B] - receiver_map[B]
                
                if A_value > B_value:
                    answer_map[A] += 1
                elif B_value > A_value:
                    answer_map[B] += 1
                
    
    return max(answer_map.values())