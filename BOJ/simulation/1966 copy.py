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
        NQ = []
        for i in range(N):
            NQ.append((i, Q[i]))

        print(NQ)
        order = 0
    
        while True:
            n_first = NQ.pop(0)
            first = Q.pop(0)
            same_doc_cnt = Q.count(first)

            if same_doc_cnt == 0:
                order += 1
                if n_first[0] == M:
                    print(order)
                    break
                else:
                    Q.append(first)
                    NQ.append(n_first)
                    continue

            Q.append(first)
            NQ.append(n_first)

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



        

            

