'''
프린터 큐
''' 
'''
세번째 풀이
'''
def solution():
   for _ in range(int(input())):
        N, M = map(int, input().split())
        Q = list(map(int, input().split()))
        NQ = [(x,idx) for idx, x in enumerate(Q)]
        if len(Q) == 1:
            # 특정입력값을 예외처리할때 return을 사용하면 나머지 입력값들은 검정할 수 없게됨. 조심할것.
            print(1)
            continue

        print_order = 0

        while True:
            # print(NQ)
            nq, nq_idx = NQ.pop(0)
            MAX = 0
            # 이런경우 이진탐색으로 시간복잡도 낮출수있음 단 데이터가 큰경우에 한함. 데이터가 작을땐 오히려 비효율적
            for val, v_idx in NQ:
                if val > nq:
                    MAX = val

            #중요도가 높은 문서가 하나라도 없는경우
            if MAX == 0:
                print_order += 1
                if nq_idx == M:
                    # print('M이랑 같지롱')
                    # print(nq_idx)
                    print(print_order)
                    break
            else:
            #중요도가 높은 문서가 하나라도 있는경우 뒤에 재배치
                NQ.append((nq, nq_idx))

solution()

'''
두번째 풀이
문제의 전제조건은 특정문서가 반드시 q에 있다는점.
'''
# def solution():
    
#     for _ in range(int(input())):
#         N, M = map(int, input().split())
#         Q = list(map(int, input().split()))
#         #중요도는 1이상 9이하이므로..
#         #엇그러면 중복되는 애들의 인덱스는????아하..이부분을 고려를 못했네
#         INDEX = [0] * 10

#         def check():
#             nonlocal Q
#             order = 0
            
#             while True:
#                 first = Q.pop(0)
#                 same_doc_cnt = Q.count(first)

#                 if same_doc_cnt == 0:
#                     order += 1
#                     if INDEX[first] == M:
#                         print(order)
#                         return
#                     else:
#                         Q.append(first)
#                         continue
#                 Q.append(first)

#         # q인덱스값 메모
#         for q_idx, q in enumerate(Q):
#             if INDEX[q] == 0:
#                 INDEX[q] == q_idx
#         check()
# solution()

'''
첫번째풀이 - 리스트 사용
'''
# def print_check(priority):
#     global print_cnt
#     while True:
#         # 0번째요소가 중요도, 1번째요소가 idx
#         reversed_priority = sorted(priority, key = lambda x: (-x[0]))
#         MAX = reversed_priority[0][0]
#         # 프린트불가능
#         if priority[0][0] < MAX:
#             priority.append(priority.pop(0))
            
#         # 프린트가능
#         else:
#             print_cnt += 1
#             if priority[0][1] == target_idx:
#                 print(print_cnt)
#                 break
#             priority.pop(0)

# for i in range(int(input())):
#     N, target_idx = map(int, input().split())
#     priority = list(map(int, input().split()))
#     # priority = [ x for x in range(5)] * 20
    
#     for i in range(N):
#         priority[i] = (priority[i],i)
#     print_cnt = 0
#     if N == 1:
#         print_cnt += 1
#         print(print_cnt)
#         continue
    
#     print_check(priority)



        

            

