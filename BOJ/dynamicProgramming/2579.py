'''
계단오르기
'''
'''
세번째풀이 - 우리가 구해야할꺼는? 밟지 않았을때의 경우의 수니까
        모든계단을 다 밟은 점수에서 밟지않았을때의 최소한의 점수만 빼주면 됨
'''
def solution():
    N = int(input())

    stairs = [0]
    total = 0
    for _ in range(N):
        num = int(input())
        stairs.append(num)
        total += num
    D = [0 for _ in range(N+1)]
    
    # 2보다 작은경우는 모든 계단 다 밟을 수 있는거니깐 점수 걍 다 합한거 출력하면 그만임
    if N <=2:
        print(total)
        return

    D[1], D[2], D[3] = stairs[1], stairs[2], stairs[3]

    for i in range(4, N):
        D[i] = min(D[i-3], D[i-2]) + stairs[i]

    print(total - min(D[N-1], D[N-2])) # N번째 계단은 당연히 안밟을꺼니깐
solution()


'''
두번째/세번째풀이 - DP, 3미만의 수 예외처리 - 인덱스에러해결
'''
# import sys
# input = sys.stdin.readline

# def solution():
#     N = int(input())
#     STAIRS = []
    
#     for _ in range(N):
#         #입력값에 \n없애주고 int형으로 변환해주는거 잊지말자..
#         STAIRS.append(int(input().rstrip()))
    
#     DP = []

#     #계단의 갯수가 3개미만인경우
#     if N == 1:
#         return STAIRS[0]
#     if N == 2:
#         return max(STAIRS[1], STAIRS[0] + STAIRS[1])
        
#     DP.append(STAIRS[0])
#     DP.append(max(STAIRS[1], STAIRS[0] + STAIRS[1]))
#     DP.append(max(STAIRS[0] + STAIRS[2], STAIRS[1] + STAIRS[2]))
    
#     for i in range(3,N):
#         DP.append( max(DP[i-2] + STAIRS[i], DP[i-3] + STAIRS[i] + STAIRS[i-1]) )

#     return DP[N-1]
# print(solution())

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