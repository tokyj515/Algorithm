from collections import deque


def solution(cacheSize, cities):
    cities = [x.lower() for x in cities]
    cache = deque()
    time = 0

    # 캐시 사이즈 0
    if cacheSize == 0:
        return len(cities) * 5

    # 캐시 사이즈 1 이상
    for city in cities:

        if len(cache) < cacheSize:
            if city not in cache:
                cache.append(city)
                time += 5
            else:
                time += 1
                cache.remove(city)
                cache.append(city)
                
        elif len(cache) >= cacheSize:
            if city not in cache:
                cache.popleft()
                cache.append(city)
                time += 5
            else:
                # 순서 바꾸기
                time += 1
                cache.remove(city)
                cache.append(city)

        # print(cache)

    return time

