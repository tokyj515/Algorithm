import heapq


def solution(operations):
    
    min_heap = []
    max_heap = []
    answer = []
    
    for i in operations:
        op, data = i.split(" ")
        data = int(data)
        
        if op == "I":
            heapq.heappush(min_heap, data) 
            heapq.heappush(max_heap, -data)
        elif len(min_heap) == 0:
            continue
        elif data == 1:
            heapq.heappop(max_heap)
            min_heap.pop()
        elif data == -1:
            heapq.heappop(min_heap)
            max_heap.pop()
    
    print(min_heap)
    print(max_heap)
    
    
    
    if len(min_heap) < 1:
        answer.append(0)
        answer.append(0)
    else:
        answer.append(-heapq.heappop(max_heap))
        answer.append(heapq.heappop(min_heap))
    
    
    
    return answer