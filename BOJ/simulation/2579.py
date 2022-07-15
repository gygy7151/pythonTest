'''
계단오르기
'''
'''
두번째/세번째풀이 - DP, 3미만의 수 예외처리 - 인덱스에러해결
'''
import sys
input = sys.stdin.readline

def solution():
    N = int(input())
    STAIRS = []
    
    for _ in range(N):
        #입력값에 \n없애주고 int형으로 변환해주는거 잊지말자..
        STAIRS.append(int(input().rstrip()))
    
    DP = []

    #계단의 갯수가 3개미만인경우
    if N == 1:
        return STAIRS[0]
    if N == 2:
        return max(STAIRS[1], STAIRS[0] + STAIRS[1])
        
    DP.append(STAIRS[0])
    DP.append(max(STAIRS[1], STAIRS[0] + STAIRS[1]))
    DP.append(max(STAIRS[0] + STAIRS[2], STAIRS[1] + STAIRS[2]))
    
    for i in range(3,N):
        DP.append( max(DP[i-2] + STAIRS[i], DP[i-3] + STAIRS[i] + STAIRS[i-1]) )

    return DP[N-1]
print(solution())

'''
첫번째풀이 - 틀림
'''
# def solution():
#     A = [0]
#     N = int(input())
    
#     for _ in range(N):
#         A.append(int(input()))

#     ANS = -1

#     TEST = [
#         [2,2],
#         [1,1,2],
#         [2,1,2],
#         [1,2,2],
#         [2,1,2,1,2,2],
#         [1,2,2,2,1,2]
#     ]

#     for i in range(6):
        
#         idx = 1
#         #아..여기가 A[0]이 아니라 A[1]이여야됨
#         res = A[1]
#         while True:
#             Fail = False
            
#             for jump in TEST[i]:
#                 idx += jump
#                 if idx > N:
#                     Fail = True
#                     break
#                 res += A[idx]

#             if Fail:
#                 break
#             ANS = max(ANS, res)

#     return ANS

# print(solution())