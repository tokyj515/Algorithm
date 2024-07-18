# t초 동안 붕대 감기 
# 1초마다 x만큼 회복 => 총 t*x만큼 회복
# t초 연속으로 붕대 감기 성공 => +y체력

# 공격 당해서 기술 취소 or 연속 성공 0으로 초기화
# 체력이 0 이하 되면 그냥 끝


def solution(bandage, health, attacks):
    # bandage: t초, 1초당 회복량, y
    # health: 최대 체력
    
    max_health = health
    
    success = 0
    time = [x[0] for x in attacks]

    
    
    for t in range(1, max(time)+1):
        # 공격 받았을 때
        if t in time: 
            
            success = 0
            
            attacked = attacks[time.index(t)][1]
            health -= attacked
            
            print("[", t, "초] 공격: ", attacked, " 체력: ", health )
            
            
        else:
            # print(t, "휴")
            # 공격받은 시간에 없으면 일단 공격에 성공한 것
            success += 1
            health += bandage[1]

    
        # health 범위 체크 ####
        # 1. 연속 성공 달성 여부 -> 추가 최복이 있기 때문
        if success == bandage[0]:
            health += bandage[2]
            success = 0
        
        # 2. max를 넘기면 max로 제한
        if health > max_health:
            health = max_health ###
        
        # 3. 0 이하면 -1
        if health <= 0:
            return -1
        
        
        
        print("[", t, "초] ", " 체력: ", health,  " 성공: ", success )
        print()

    

    
    return health
    
    
    