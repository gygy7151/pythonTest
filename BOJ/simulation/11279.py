'''
최대힙
'''
'''
번외 - 최소힙문제
비커에 일정 T이상 물이 담기도록 액체가 가장 적게담긴 두비커의 액체를 합쳐나가기.
Test CASES
- L : [1,2,3,4,5,6,7] , T: 4 # 2
- L : [3,5,1,8,3,2,1,9], T: 7 # 5
- L : [3,5,1,8,3,2,1,9], T: 50 # -1케이스
'''
import heapq
def solution():
    T = int(input())
    L = list(map(int, input().split()))
    heapq.heapify(L)

    def check():
        for l in L:
            if l < T:
                return False
        return True
    
    CNT = 0
    while len(L) >= 2:
        A, B = heapq.heappop(L), heapq.heappop(L)
        heapq.heappush(L, A+B)
        CNT += 1
        if check():
            return CNT

    return -1
print(solution())
'''
두번째풀이- 최대힙으로구현 (최소힙 변형 heapq라이브러리활용)
'''
# import sys
# import heapq
# input = sys.stdin.readline

# def solution():
#     N = int(input())
#     MAX_HEAP = []
    
#     for _  in range(N):
#         num = int(input())
        
#         if num == 0:
#             if len(MAX_HEAP):
#                 MAX_ITEM = heapq.heappop(MAX_HEAP)[1]
#                 print(MAX_ITEM)
#             else:
#                 print(0)
#         else:
#             heapq.heappush(MAX_HEAP, (-num, num))
    
# solution()

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