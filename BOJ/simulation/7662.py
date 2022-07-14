'''
이중우선순위큐
'''

'''
다섯째풀이
'''
# import sys
# import heapq
# input = sys.stdin.readline


# test = int(input())
# for _ in range(test):
#     max_heap, min_heap = [], []
#     visit = [False] * 1_000_001

#     order_num = int(input())

#     for key in range(order_num):
#         order = input().rsplit()
#         if order[0] == 'I':
#             heapq.heappush(min_heap, (int(order[1]), key))
#             heapq.heappush(max_heap, (int(order[1]) * -1, key))
#             visit[key] = True #True이면 어떤 힙에서도 아직 삭제되지 않은 상태

#         elif order[0] == 'D':
#             if order[1] == '-1': #삭제연산시, key값을 기준으로 해당 노드가 다른힙에서 삭제된 노드인가를 먼저 판단한다.
#                 # 이미 상대힙에 의해 삭제된 노드인경우 삭제되지 않은 노드가 나올때까지 계쏙 버리다가 이후 삭제대상노드가 나오면 삭제한다.
#                 while min_heap and not visit[min_heap[0][1]]: # visit이 False일떄 -> 해당노드가 삭제된상태
#                     heapq.heappop(min_heap) # 버림 (상대힙에서 이미 삭제된노드이므로)
#                 if min_heap:
#                     visit[min_heap[0][1]] = False # visit이 Ture엿으므로 False로 바꾸고 내가 삭제함
#                     heapq.heappop(min_heap)
#             elif order[1] == '1':
#                 while max_heap and not visit[max_heap[0][1]]: #이미 삭제된 노드인경우 삭제되지 않은 노드가 나올때까지 모두 버린다.
#                     heapq.heappop(max_heap)
#                 if max_heap:
#                     visit[max_heap[0][1]] = False
#                     heapq.heappop(max_heap)

# # 모든 연산이 끝난후에도 ㅅ쓰레기 노드가 들어있을수 있으므로, 결과를 내기전 모두 비우고 각 힙의 첫번째 원소값을 출력한다. 
#     while min_heap and not visit[min_heap[0][1]]:
#         heapq.heappop(min_heap)
#     while max_heap and not visit[max_heap[0][1]]:
#         heapq.heappop(max_heap)

#     if min_heap and max_heap:
#         print(-max_heap[0][0], min_heap[0][0])
#     else:
#         print('EMPTY')

'''
네번째풀이 - id값을 넣어주어 키값을 토대로 최소힙과 최대힙을 동기화시켜준다 -시간초과
'''
import sys
import heapq
input = sys.stdin.readline

for _ in range(int(input())):
    MEMO = [False] * 1000001
    MIN_H, MAX_H = [], []

    for id in range(int(input())):
        O, N = input().split()

        if O == 'I':
            heapq.heappush(MIN_H, (int(N), id))
            heapq.heappush(MAX_H, (-int(N), id))
            MEMO[id] = True

        #최댓값삭제
        elif N == '1':

            while MAX_H and not MEMO[MAX_H[0][1]]:
                heapq.heappop(MAX_H)
            
            
            if MAX_H:
                MEMO[MAX_H[0][1]] = False
                heapq.heappop(MAX_H)
        #최솟값삭제
        else:
            while MIN_H and not MEMO[MIN_H[0][1]]:
                heapq.heappop(MIN_H)
            

            if MIN_H:
                MEMO[MIN_H[0][1]] = False
                heapq.heappop(MIN_H)

    while MIN_H and not MEMO[MIN_H[0][1]]:
        heapq.heappop(MIN_H)
    
    while MAX_H and not MEMO[MAX_H[0][1]]:
        heapq.heappop(MAX_H)
    
    if MAX_H and MIN_H:
        print(-MAX_H[0][0], MIN_H[0][0])

    else:
        print('EMPTY')

            



'''
두번째/세번째풀이 - maxheap, minheap 합쳐서 풀어보기 - 둘이든 하나든 시간초과남..
'''
# import sys
# import heapq
# input = sys.stdin.readline

# def priority():
#     Q = []
#     heapq.heapify(Q)

#     for _ in range(int(input())):
#         O, N = map(str, input().split())

#         if O == 'I':
#             heapq.heappush(Q, int(N))
        
#         else:
#             if len(Q):
#                 #최솟값삭제
#                 if N == '-1':
#                     if len(Q):
#                         heapq.heappop(Q)
#                 #최댓값삭제
#                 else:
#                     if len(Q):
#                     #(마지막인덱스/미포함임, 이터러블객체)[리스트인덱스요소 자르기, 여러개도가능]
#                         Q.pop(Q.index(heapq.nlargest(1, Q)[0]))

    
#     if len(Q):
#         return ' '.join(map(str, [heapq.nlargest(1, Q)[0], heapq.nsmallest(1, Q)[0]]))


#     else:
#         return 'EMPTY'
    
# def solution():
#     for _ in range(int(input())):
#         print(priority())
        
# solution()





'''
첫번째풀이 - heapq 사용안하고 풀었는데 3%에서 틀림..
'''
# import sys
# from collections import deque
# input = sys.stdin.readline

# def solution():
    
#     for _ in range(int(input())):
#         Q = deque()
#         for _ in range(int(input())):

#             CAL, N = map(str, input().split())
            
#             if CAL == 'I':
#                 #동일한 정수도 삽입될 수 있는걸 고려못했다.. =을 추가해줌
#                 if len(Q):
#                     if Q[-1] <= int(N):
#                         Q.append(int(N))
#                     elif Q[0] >= int(N):
#                         Q.appendleft(int(N))

#                 else:
#                     Q.append(int(N))
#                     Q = list(Q)
#                     Q.sort()
#                     Q = deque(Q)

#             else:
#                 if len(Q):
#                     if N == '1':
#                         Q.pop()

#                     else:
#                         Q.popleft()
        
#         #Q에 남은값중 최댓최솟값출력
#         if len(Q):
#             print(Q[-1], Q[0], sep=" ")
        
#         else:
#             print('EMPTY')

# solution()

