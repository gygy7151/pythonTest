'''
캐시
'''
'''
첫번째풀이
'''
def solution(cacheSize, cities):
    if cacheSize == 0:
        return 5*len(cities)
    
    cache = []
    answer = 0

    for city in cities:
        lo_city = city.lower()
        
        try:
            idx = cache.index(lo_city)
            cache.append(cache.pop(idx))
            answer += 1
            
        except:
            cache.append(lo_city)
            
            if len(cache) > cacheSize:
                cache.pop(0)
            
            answer += 5
            

    return answer