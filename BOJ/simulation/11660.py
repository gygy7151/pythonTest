'''
구간합구하기 5
'''
'''
참조코드
'''
# import sys
# input = sys.stdin.readline

# def solution():
#     N, M = map(int, input().split())
#     A = list(map(int, input().split()))

#     #변수를 활용해 이전값 차근차근더해줄것
#     sum_val = 0
#     #연결리스트로 접두사합 추가해주고
#     P = [0]
#     for num in A:
#         sum_val += num
#         P.append(sum_val)
    
#     for _ in range(M):
#         left, right = map(int, input().split())
#         print(P[right] - P[left-1])

# solution()
'''
세번째풀이 - 틀림
'''
import sys
input = sys.stdin.readline

def solution():
    N, M = map(int, input().split())
    G = [[0 for _ in range(N+1)]]

    for _ in range(N):
        data = [0] + list(map(int, input().split()))
        G.append(data)
    
    #행부터 더하기
    for i in range(1,N+1):
        for j in range(1,N):
            G[i][j+1] += G[i][j]
    
    #열끼리 더하기
    for j in range(1,N+1):
        for i in range(1,N):
            G[i+1][j] += G[i][j]

    for _ in range(M):
        x1, y1, x2, y2 = map(int, input().split())
        print(G[x2][y2] - (G[x1-1][y2] + G[x2][y1-1]) + G[x1-1][y1-1])
solution()


'''
두번째풀이 - DP - 시간초과
'''
# import sys
# input = sys.stdin.readline

# def solution():
#     N, M = map(int, input().split())
#     DP = [[] for _ in range(N)]
    
#     for i in range(N):
#         sumVal = 0
#         data = list(map(int, input().split()))

#         for a in data:
#             sumVal += a
#             DP[i].append(sumVal)

#     for _ in range(M):
#         x1, y1, x2, y2 = map(int, input().split())
#         answer = 0
#         x2 -= 1
#         while x2 > -1:
#             if y1 == 1:
#                 answer += DP[x2][y2-1]
#             else:
#                 answer += (DP[x2][y2-1] - DP[x2][y1-2])
#             x2 -= 1
        
#         print(answer)

# solution()

    


    


    

    



'''
첫번째풀이 - 시간초과
'''
# import sys
# input = sys.stdin.readline

# def solution():
#     N, M = map(int, input().split())
#     G = []
#     DP = []
    
#     for _ in range(N):
#         G.append(list(map(int, input().split())))
    
#     for _ in range(M):
#         x1, y1, x2, y2 = map(int, input().split())
#         res = 0

#         for i in range(x1-1, x2):
#             res += sum(G[i][y1-1:y2])

#         print(res)

# solution()
