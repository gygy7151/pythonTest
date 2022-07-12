'''
최대힙
'''
'''
두번째풀이- 최대힙으로구현 (최소힙 변형 heapq라이브러리활용)
'''
import sys
import heapq
input = sys.stdin.readline

def solution():
    N = int(input())
    MAX_HEAP = []
    
    for _  in range(N):
        num = int(input())
        
        if num == 0:
            if len(MAX_HEAP):
                MAX_ITEM = heapq.heappop(MAX_HEAP)[1]
                print(MAX_ITEM)
            else:
                print(0)
        else:
            heapq.heappush(MAX_HEAP, (-num, num))
    
solution()

'''
첫번째풀이 - 시간초과
'''
# import sys
# input = sys.stdin.readline

# def solution():
#     N = int(input())
#     A = []
    
#     for _  in range(N):
#         num = int(input())
        
#         if num == 0:
#             if len(A):
#                 print(max(A))
#                 A.pop(A.index(max(A)))
#             else:
#                 print(0)
#         else:
#             A.append(num)
    
# solution()