import heapq

# 오름차순
def heapsort_increase(iterable) :

    h = []

    result = []

    #모든 원소를 차례대로 힙에 삽입

    for value in iterable :

        heapq.heappush(h, value)

    for i in range(len(h)) :

        result.append(heapq.heappop(h))
    
    return result


def heapsort_decrease(iterable):
    h = []

    result = []

    #모든 원소를 차례대로 힙에 삽입

    for value in iterable :

        heapq.heappush(h, -value)

    for i in range(len(h)) :

        result.append(-heapq.heappop(h))
    
    return result



result = heapsort_increase([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
print(result)

resultt = heapsort_decrease([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
print(resultt)

