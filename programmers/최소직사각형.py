'''
최소직사각형
'''
'''
네번째풀이
'''
def solution(sizes):
    return max(max(x) for x in sizes) * max(min(x) for x in sizes)

A = [[80, 40], [20,50], [60,30]]
print(solution(A))
'''
세번째풀이 - 너무 길고, 일부 테스트케이스 틀림
'''
# from collections import deque
# import copy
# def solution(sizes):
#     size = copy.deepcopy(sizes)
#     answer = 0
#     n_sizes = list(map(list, zip(*size)))
#     MW, MH = max(n_sizes[0]), max(n_sizes[1])
#     order = deque()
#     NMW, NMH = 0,0
    
#     def switch(case):
#         nonlocal NMW
#         nonlocal NMH
#         nonlocal MW
#         nonlocal MH
#         nonlocal order
#         nonlocal size
#         nonlocal answer
#         nonlocal n_sizes

#         order = sorted(order, key=lambda x : (-x[0]))

#         for i in range(len(sizes)):
#             idx = order[i][1]
#             w = size[idx][0]
#             h = size[idx][1]
#             # MW > MH : 제일 작은합을 만드는 최대h값 찾는게 목표
#             if case == 'A':
#                 if w > h:
#                     break

#                 elif w < h:
#                     # ***아..실재 리스트값을 바꿀려면 해당요소 직접 할당해줘야됨.
#                     size[idx][0], size[idx][1] = h, w
#                     n_sizes = list(map(list, zip(*size)))
#                     NMH = max(n_sizes[1])
#                     NMH = min(NMH, MH)
#                     answer = min(MW*MH, MW*NMH)

#             # MW < MH :제일 작은합을 만드는 최대w값 찾는게 목표
#             else:
#                 if h > w:
#                     break
            
#                 elif h < w:
#                     size[idx][0], size[idx][1] = h, w
#                     n_sizes = list(map(list, zip(*size)))
#                     NMW = max(n_sizes[0])
#                     NMW = min(NMW, MW)
#                     answer = min(MW*MH, NMW*MH)

#     # A
#     if MW > MH:
        
#         for cnt, h in enumerate(n_sizes[1]):
#             order.append((h,cnt))
#             cnt+= 1
    
#         switch('A')
        
#     # B     
#     elif MW < MH:
#         for cnt, w in enumerate(n_sizes[0]):
#             order.append((w,cnt))
        
#         switch('B')
        
#     else:
#         answer = MW * MH
#         return answer
    
#     return answer

# A = [[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]
# print(solution(A))



















'''
첫번째풀이 - 답이 이상하게 나옴.. 모듈화가 필요함 너무 길고 복잡해..내가봐도 짜증나는 코드임..하..
'''

'''
두번째풀이 - 2가지 경우만 생각했더니 다른 테케에서 틀리게 나옴..
'''
# import copy
# def solution(sizes):
#     # print(sizes)
#     answer = 0
#     # (길이, 인덱스)
#     w_max, h_max = [0,0], [0,0]
    
#     # 최대 가로 세로 먼저 구함
#     idx = 0
#     for w, h in sizes:
#         if w > w_max[0]:
#             w_max = [w, idx]
#         if h > h_max[0]:
#             h_max = [h, idx]
#         idx += 1
#     # print(w_max, h_max)
    
#     # 최대가로 변형
#     n_sizes = copy.deepcopy(sizes)
#     n_sizes[w_max[1]] = [sizes[w_max[1]][1] , sizes[w_max[1]][0]]
#     # print(n_sizes)
#     # 새로운 최대 가로 세로 구함
#     Anw_max, Anh_max = [0,0], [0,0]
#     idx = 0
#     for w, h in n_sizes:
#         if w > Anw_max[0]:
#             Anw_max = [w, idx]
#         if h > Anh_max[0]:
#             Anh_max = [h, idx]
#         idx += 1
      
#     # 최대 세로 변형
#     n_sizes = copy.deepcopy(sizes)
#     n_sizes[h_max[1]] = [sizes[h_max[1]][1] , sizes[h_max[1]][0]]
#     # print(n_sizes)
#     # 새로운 최대 가로 세로 구함
#     Bnw_max, Bnh_max = [0,0], [0,0]
#     idx = 0
#     for w, h in n_sizes:
#         if w > Bnw_max[0]:
#             Bnw_max = [w, idx]
#         if h > Bnh_max[0]:
#             Bnh_max = [h, idx]
#         idx += 1
#     # print(Bnw_max,Bnh_max)
#     # 가로세로 변형 최대 크기 비교
#     A, B = Anw_max[0] * Anh_max[0], Bnw_max[0] * Bnh_max[0]
#     # print(A,B)

#     if A > B:
#         nw_max, nh_max = Bnw_max[0], Bnh_max[0]

#     elif A < B:
#         nw_max, nh_max = Anw_max[0], Anh_max[0]
    
#     else:
#         nw_max, nh_max = w_max[0], h_max[0]
    
#     # 기존 가로세로와 변형 최대가로세로 크기 비교
#     A, B = (w_max[0]*h_max[0]), (nw_max * nh_max) 
    
#     if A > B:
#         answer = B

#     elif A < B:
#         answer = A
    
#     else:
#         answer = (nw_max * nh_max)
#     return answer
# A = [[60, 50], [30, 70], [60, 30], [80, 40]]
# print(solution(A))