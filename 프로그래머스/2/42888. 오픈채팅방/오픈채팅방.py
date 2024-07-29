def solution(record):
    # 닉네임 변경 방법
    # 1. 채팅방을 나가고 다시 들어가기
    # 2. 채팅방 안에서 닉네임 변경하기
    
    name = {}
    result = []
    
    action = {"Enter": "님이 들어왔습니다.", "Leave": "님이 나갔습니다."}
    
    
    for r in record:
        r = r.rstrip().split(" ")
        if len(r) == 3:
            name[r[1]] = r[2]
        
    for r in record:
        r = r.rstrip().split(" ")
        
        if r[0] == 'Enter':
            result.append(name[r[1]] + action[r[0]])
        elif r[0] == 'Leave':
            result.append(name[r[1]] + action[r[0]])
            
    return result
            