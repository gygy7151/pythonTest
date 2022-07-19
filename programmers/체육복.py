'''
체육복
'''
'''
다섯번째풀이 - 맞음
'''
def solution(n, lost, reserve):
    answer = 0
    A, B = set(lost), set(reserve)
    lost = list(A - B)
    reserve = list(B - A)
    
    for i in lost:
        a = i - 1
        b = i + 1
        for j in reserve:
            if j == a or j == b:
                reserve.remove(j)
                answer += 1
                break
            
    return n - len(lost) + answer


'''
네번째풀이 - 성공
'''
def solution(n, lost, reserve):
    A, B = set(lost), set(reserve)
    lost = list(A - B)
    reserve = list(B - A)
    R = {i:True for i in reserve}
    L = {i:True for i in lost}
    
    for i in lost:
        a = i - 1
        b = i + 1
        for j in reserve:
            if a == j and R[j]:
                R[j] = False
                L[i] = False
                break
                
            elif b == j and R[j]:
                R[j] = False
                L[i] = False
                break
    
    
    return n - list(L.values()).count(True)

'''
세번째풀이 - 실패
'''
# def solution(n, lost, reserve):
#     answer = 0
#     P = {}
#     for i in lost:
#         P[i] = 1
#         P[i] -= 1
        
#     for i in reserve:
#         P[i] = 1
#         P[i] += 1
    
#     print(P)
#     if n == 2:
#         M = list(P.values()).count(0)
#         if M == 2:
#             return 0
#         elif M == 1:
#             return 1
            
#         else:
#             return 2
    
      
#     for i in lost:
#         try:
#             if P[i+1] == 2:
#                 P[i+1] -= 1
#                 P[i] = 1
#         except:
#             try:
#                 if P[i-1] == 2:
#                     P[i-1] -= 1
#                     P[i] = 1
#             except:
#                 pass
                
#     print(P)
#     return n - list(P.values()).count(0)
'''
첫번째/두번째풀이 - 틀림
'''
# def solution(n, lost, reserve):
#     answer = 0
#     P = {i:1 for i in range(1,n+1)}
    
#     for i in lost:
#         P[i] -= 1
        
#     for i in reserve:
#         P[i] += 1
    
    
#     if n == 2:
#         M = list(P.values()).count(0)
#         if M == 2:
#             return 0
#         elif M == 1:
#             return 1
            
#         else:
#             return 2
      
#     for i in lost:
#         if 2 <= i <= n-1:
#             if P[i-1] == 2:
#                 P[i-1] = 1
#                 P[i] = 1
#             elif P[i+1] == 2:
#                 P[i+1] = 1
#                 P[i] = 1
#         elif i == 1:
#             if P[i+1] == 2:
#                 P[i+1] = 1
#                 P[i] = 1
#         else:
#             if P[i-1] == 2:
#                 P[i-1] = 1
#                 P[i] = 1
#     print(P)
#     return n - list(P.values()).count(0)