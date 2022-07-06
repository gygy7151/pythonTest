'''
덩치
'''
'''
세번째풀이
'''
def solution():
    import sys
    input = sys.stdin.readline
    N = int(input())
    INFO = []

    for ID in range(N):
        W, H = map(int, input().split())
        INFO.append((W,H,ID))

    #오름차순정렬
    INFO.sort(key= lambda x: (x[0],x[1]))
    # print(INFO)
    #등수매기기
    GRADE = [0] * N
    for x, y, id in INFO:
        k = 0 # 문제에서 등수라고 지칭했음
        for i in range(1, N):
            nx, ny, nid = INFO[i]

            if x < nx and y < ny:
                k += 1
        
        #자기자신보다 큰사람이 아무도 없다는 뜻이므로
        #아..k조건을 초기화 값이랑 변경하면서 같이 얘외조건 변경하지 못했다.. 1에서 0으로 바꿨는데..
        
        if k == 0:
            GRADE[id] = 1

        else:
            GRADE[id] = k+1
    
    return GRADE
res = solution()
print(*res, sep=' ')

'''
첫번째 풀이, 두번째풀이 - 틀림 등수매기는 로직이 이상했음
'''
# import sys
# input = sys.stdin.readline
# def solution():
#     N = int(input())
#     INFO = []
    
#     # 내림차순정렬
#     for ID in range(N):
#         W, H = map(int, input().rsplit())
#         INFO.append((W,H,ID))
#     INFO.sort(key=lambda x: (-x[0], -x[1]))
#     print(INFO)
    
#     #등수매기기
#     GRADE = [0] * (N)
#     #미리 1등은 등수 초기화 시켜준다.
#     GRADE[INFO[0][2]] = 1
    
#     for k in range(1,N):
#         #0:무게,1:키,2:id
#         A = INFO[k-1]
#         B = INFO[k]

#         # 몸무게는 작은데 키는 같은 경우
#         if B[0] < A[0] and B[1] == A[1]:
#             GRADE[B[2]] = k+1
#             A = INFO[k]
#         # 키는 작은데 몸무게는 같은 경우
#         elif B[1] < A[1] and B[0] == A[0]:
#             GRADE[B[2]] = k+1
#             A = INFO[k]
        
#         # 몸무게랑 키 모두 작은경우   
#         elif B[0]< A[0] and B[1] < A[1]:
#             GRADE[B[2]] = k+1
#             A = INFO[k]
#         else:
#             #몸무게랑 키 모두 같은경우
#             #몸무게랑 키 모두 큰 경우
#             GRADE[B[2]] = GRADE[A[2]]

#     return GRADE
# res = solution()
# print(*res, sep=' ')