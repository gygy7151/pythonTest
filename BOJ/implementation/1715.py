'''
카드 정렬하기
'''
'''
첫번째풀이
'''
import heapq
import sys
input = sys.stdin.readline
def solution():
    N = int(input())
    arr = []
    
    for _ in range(N):
        heapq.heappush(arr, int(input()))

    
    if len(arr) == 1:
        print(0)
            
    else:
        answer = 0

        while len(arr) > 1:
            temp_1 = heapq.heappop(arr) # 제일 작은 덱
            temp_2 = heapq.heappop(arr) # 두번째로 작은 덱
            answer += temp_1 + temp_2
            heapq.heappush(arr, temp_1 + temp_2)
        
        print(answer)
solution()
