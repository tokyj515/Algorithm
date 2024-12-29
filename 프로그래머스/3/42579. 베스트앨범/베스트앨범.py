from collections import defaultdict

def solution(genres, plays):
    answer = []
    
    # 각 장르의 총 재생 수와 장르별 곡 리스트를 저장
    hap = defaultdict(int)
    dic = defaultdict(list)
    
    for i in range(len(genres)):
        hap[genres[i]] += plays[i]  
        dic[genres[i]].append([plays[i], i])

    
    hap = dict(sorted(hap.items(), key=lambda item: item[1], reverse=True))
    
    for g in dic:
        dic[g].sort(key=lambda x: -x[0])  
    
    
    for g in hap:
        music = dic[g]
        for i in range(min(2, len(music))): 
            answer.append(music[i][1])
    
    return answer