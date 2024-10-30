from heapq import heapify, heappush, heappop

def solution(book_time):
    
    def calc(time):
        h, m = map(int, time.split(":"))
        return h*60+m
    
    for i in range(len(book_time)):
        start, end = book_time[i]
        book_time[i][0] = calc(start)
        book_time[i][1] = calc(end)+10
    
    book_time.sort()
    
    print(book_time)
        
        
    room = [] # 방
        
    for start, end in book_time:
        if room and room[0] <= start:
            heappop(room)
            
        heappush(room, end)
    
    return len(room)
        
        
        
        
    
    