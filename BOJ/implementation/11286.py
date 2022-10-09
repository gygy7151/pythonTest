'''
절대값 힙
'''
'''
첫번째풀이
'''
import heapq
def solution():
    N = int(input())
    arr = []
    
    for _ in range(N):
        action = int(input())

        # 배열에 x를 추가하는 연산
        if action != 0:
            heapq.heappush(arr, (abs(action),action))
        
        # 배열에 절댓값이 가장 작은 값을 출력 그값을 제거
        else:
            if not arr:
                print(0)
            else:
                print(heapq.heappop(arr))

solution()
