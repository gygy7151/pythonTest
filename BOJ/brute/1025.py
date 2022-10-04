'''
제곱수 찾기
'''
'''
두번째풀이 - sqrt쓰지말구 그냥 직접하셈 
'''
import sys
input = sys.stdin.readline

def solution():
    N, M = map(int, input().split())
    board = [list(input().strip()) for _ in range(N)]
    answer = -1

    # 기능을 따로 모듈화 한게 넘 좋은 접근임
    def sqrt(S):
        S = int(S)
        return int(S ** 0.5) ** 2 == S
    
    for i in range(N): # 행 시작 좌표
        for j in range(M): # 열 시작 좌표
            for row_d in range(-N, N): # 행의 공차
                for col_d in range(-M, M): # 열의 공차
                    S = ''
                    x,y = i,j
                    if row_d == 0 and col_d == 0:
                        continue
                    
                    while 0 <= x < N and 0 <= y < M:
                        S += board[x][y]
                        # 제곱수 확인을 모듈화한 접근이 에러 안나고 좋음
                        if sqrt(S):
                            answer = max(answer, int(S))
                        
                        x += row_d
                        y += col_d
    print(answer)    

solution()

'''
첫번째풀이 - 틀림
'''
# import sys
# from math import sqrt
# def solution():
#     N, M = map(int, input().split())
#     nums = []

#     for _ in range(N):
#         nums.append(list(input().rstrip()))

#     # 제곱가능한 수가 하나도 없는경우 -1 리턴하도로 -1로 초기화   
#     res = -1

#     for m in range(M): # 시작 행 위치
#         for n in range(N): # 시작 열 위치
#             for a in range(-N, N): # 행 방향 등차 a
#                 for b in range(-M, M): # 열 방향 등차 b
#                     num = '' # nums 그래프 모든숫자는 str 타입임.
#                     x, y = m, n # 행 x, 열 y

#                     # 행과 열 시작 위치부터 등차를 더해가며 숫자 생성
#                     while 0 <= x < N and 0 <= y < M:
#                         num += nums[x][y]
#                         if a == 0 and b == 0:
#                             break
                        
#                         # 제곱근을 다시 제곱한 수가 현재 수와 같으면 제곱수가 된다는 걸로 확인하고 res값을 갱신해줌
#                         if sqrt(int(num)) ** 2 == int(num):
#                             res = max(int(num), res)
                        
#                         #행과 열의 위치에 각각의 공차a와 b 더해줌
#                         x += a
#                         y += b

#     print(res)

# solution()