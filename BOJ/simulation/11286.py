'''
절댓값힙
'''
'''
두번째풀이 - 최소힙에 입력값만 조정해서 우선순위로 넣어주면 끝나는 문제였음..
'''
import sys
import heapq
input = sys.stdin.readline

def solution():
    orderCount = int(input())
    A = []
    heapq.heapify(A)

    for _ in range(orderCount):
        
        N = int(input())
        
        if N != 0:
            heapq.heappush(A, (abs(N), N))
        
        else:
            if A:
                print(heapq.heappop(A)[1])
            
            else:
                print(0)
solution()


        

'''
첫번째풀이 - 믹스힙으로 접근했는데 틀렸음
'''
# import sys
# import heapq
# input = sys.stdin.readline

# def solution():
#     orderCount = int(input())
#     MAX, MIN = [], []
#     heapq.heapify(MAX)
#     heapq.heapify(MIN)
#     MEMO = [False for _ in range(orderCount)]

#     for id in range(orderCount):
#         N = int(input())
        
#         if N != 0:
#             heapq.heappush(MAX, (-N, id))
#             heapq.heappush(MIN, (N, id))
#             MEMO[id] = True
#             # print(MAX)
#             # print(MIN)

#         else:
#             # print('id : {}'.format(id))
#             if MAX and MIN:
#                 # print('MAX:{} MIN:{}'.format(MAX[0][0],MIN[0][0]))
#                 # print('현재MAX구성: {}, 현재MIN구성: {}'.format(MAX, MIN))

#                 if abs(MAX[0][0]) >= abs(MIN[0][0]):
#                     #최소힙만 삭제
#                     while MIN and not MEMO[MIN[0][1]]:
#                         heapq.heappop(MIN)
                    
#                     if MIN:
#                         MEMO[MIN[0][1]] = False
#                         print(heapq.heappop(MIN))
#                         # print('MIN삭제된신규구성:{}'.format(MIN))


#                 else:
#                     #최대힙만 삭제
#                     while MAX and not MEMO[MAX[0][1]]:
#                         heapq.heappop(MAX)
                    
#                     if MAX:
#                         MEMO[MAX[0][1]] = False
#                         print(heapq.heappop(MAX))
#                         # print('MAX삭제된신규구성:{}'.format(MAX))
                    
#             else:
#                 if MIN:
#                     while MIN and not MEMO[MIN[0][1]]:
#                         heapq.heappop(MIN)
                    
#                     if MIN:
#                         MEMO[MIN[0][1]] = False
#                         print(heapq.heappop(MIN))
#                 else:
#                     print(0)
# solution()

