'''
트리의 부모 찾기
'''
'''
두번째 풀이  - 링크드 리스트이용
'''
def solution():
    N = int(input())
    # ***실수주의 [] * (N+1)해주면 => [[]...[]]이 아닌 []이게됨.
    T = [[] for _ in range(N+1)]
    MEMO = [0] * (N+1)

    for _ in range(N-1):
        A, B = map(int, input().split())
        T[A].append(B)
        T[B].append(A)
    
    Q = [1]

    while Q:
        A = Q.pop(0)
        
        for B_idx in range(len(T[A])):
            B = T[A][B_idx]
            if MEMO[B] == 0:
                MEMO[B] = A
                Q.append(B)
                
    for i in range(2, N+1):
        print(MEMO[i])

solution()




'''
첫번째 풀이 - 메모리 초과
'''
# def solution():
#     N = int(input())
#     T = [[0] * (N+1) for _ in range(N+1)]
#     MEMO = [0] * (N+1)

#     # 연결표시
#     for _ in range(N-1):
#         A, B = map(int, input().split())
#         T[A][B] = 1
#         T[B][A] = 1
    
#     q = [1]
    
#     while q:
#         A = q.pop(0)
        
#         for B in range(1, N+1):
            
#             if T[A][B] == 1 and B != 1:
            
#                 if MEMO[B] == 0:
#                     MEMO[B] = A
#                     q.append(B)
        
#     for i in range(2,N+1):
#         print(MEMO[i])

# solution()



