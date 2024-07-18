import math

def solution(fees, records):
    
    # 시간 -> 분으로 계산
    def cal_time(a, b):
        minute = 0
        in_hour, in_min = map(int, a.split(":"))
        out_hour, out_min =  map(int, b.split(":"))
        
        if out_min < in_min:
            out_hour -= 1
            out_min += 60
        
        minute += (out_hour-in_hour)*60 + (out_min-in_min)
        
        return minute
    
    
    
    
    # 변수 선언
    answer = []
    record_dict = {}
    time_dict = {}
    
    
    # record_dict 선언 후 차량 번호로 정렬
    for r in records:
        temp = r.split(" ")
        record_dict[temp[1]] = []
        
    for r in records:
        temp = r.split(" ")
        record_dict[temp[1]].append(temp[0])

    record_dict = dict(sorted(record_dict.items()))
    
    
    # 시간 -> 분으로 변경해서 time_dict로 선언
    for e in record_dict.keys():
        time = record_dict[e]
        time_dict[e] = 0
        
        if len(time) % 2:
            time.append('23:59')
        
        for i in range(0, len(time), 2):
            a, b = time[i], time[i+1]
            time_dict[e] += cal_time(a, b)


    
    # time_dict과 fees 이용해서 발생 요금 계산
    for e in time_dict.keys():
        minute = 0
        
        if time_dict[e] <= fees[0]:
            minute += fees[1]
        else:
            minute += fees[1] + (math.ceil((time_dict[e]-fees[0])/fees[2]) * fees[3])
        
        answer.append(minute)
    
    
    
    return answer