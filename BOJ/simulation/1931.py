'''
회의실배정
'''
'''
두번째풀이 - 람다기준을 잘못세웠음.
나는 시간차를 우선으로 기준했었는데
제일 빨리 끝나는 시간대를 1순위
그리고 끝나는 시간대와 시작시간대의 간격을 최소화하기 위해서
시작시간이 빠른 시간대를 2순위로 정렬해주어야 했음
그리고나서 이전 시간보다 시작시간이 크거나 같으면 CNT해주면 끝나는 문제임
이중 삼중 for문 돌 필요가 없었음
'''
import sys
input = sys.stdin.readline

def solution():
    N = int(input())
    TIMES = []
    
    for i in range(N):
        TIMES.append(list(map(int, input().split())))
    
    TIMES.sort(key=lambda x:( x[1], x[0]))

    CNT = 0    
    pre_end = 0

    for time in TIMES:
        start, end = time[0], time[1]

        if start >= pre_end:
            CNT+= 1

            pre_end = end
    
    return CNT

print(solution())
            

'''
첫번째풀이- 틀림
'''
# import sys
# input = sys.stdin.readline
# def solution():
#     N = int(input())
#     TIME_TABLE = []

#     for _ in range(N):
#         start, end = map(int, input().split())
#         total_times = end - start
#         TIME_TABLE.append((start, end, total_times))

#     TIME_TABLE.sort(key=lambda x: (x[2], x[0]))

#     ROOM = {}
#     ANS = 0
#     for begin, stop, total in TIME_TABLE:

#         if begin == stop:
#             continue
#         try:
#             if ROOM[begin] and ROOM[stop]:
#                 pass
#         except:
#             RESERVATION = True
#             for i in range(begin,stop):
#                 try:
#                     if ROOM[i]:
#                         RESERVATION = False
#                         break
#                 except:
#                     ROOM[i] = 1
        
#             if RESERVATION:
#                 ANS += 1
#         return ANS
# print(solution())