'''
강의실
'''
'''
첫번째풀이
'''
import sys
import heapq
input = sys.stdin.readline


# 매번 강의를 탐색할때마다 최소힙의 개수를 구해 이의 최대값을 구한뒤 출력한다.
def solution():
    N = int(input())
    # x[0]: 강의번호, x[1]: 시작시간, x[2]: 종료시간
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 강의 시작 시간을 기준으로 오름차순 정렬한뒤 이를 하나씩 탐색한다.
    arr.sort(key=lambda x: (x[1]))

    # 최소힙
    min_h = []
    count = 0

    # 강의 끝나는 시간을 기준으로 최소힙을 구성해 시작시간보다 일찍 끝나는 강의는 모두 뺀다 왜?
    # 이전꺼니깐 연결지을 수 없어서 그런거아님?
    for x in arr:
        while min_h and min_h[0] <= x[1]: #min_h도 종료시간임
            heapq.heappop(min_h)
        
        #그리고 시작시간보다 늦게끝나는게발견된 경우 즉시 끝나는 시간 큐에 추가해줌.. 와 아름답다.
        heapq.heappush(min_h, x[2])
        count = max(count, len(min_h))
    
    print(count)
solution()



