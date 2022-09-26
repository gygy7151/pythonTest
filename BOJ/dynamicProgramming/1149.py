'''
RGB거리
'''
'''
세번째풀이
'''
def solution():
    N = int(input())
    house = [[0 for _ in range(3)] for _ in range(N+1)]
    
    for i in range(1,N+1):
        R, G, B = list(map(int, input().split()))
        house[i][0] = R
        house[i][1] = G
        house[i][2] = B
    
    dp = [[0 for _ in range(3)] for _ in range(N+1)]
    dp[1][0], dp[1][1], dp[1][2] = house[1][0], house[1][1], house[1][2]

    for i in range(2, N+1):
        dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + house[i][0]
        dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + house[i][1]
        dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + house[i][2]

    print(min(dp[N]))
solution()
    
'''
두번째풀이 -DP
'''
# def solution():
#     RGB = []
#     N = int(input())

#     for _ in range(N):
#         RGB.append(list(map(int, input().split())))

#     for r in range(1, N):
#         #j는 i열
#         for c in range(3):
#             if c == 0:
#                 RGB[r][c] = min(RGB[r-1][1]+RGB[r][c], RGB[r-1][2]+RGB[r][c])
#             elif c == 1:
#                 RGB[r][c] = min(RGB[r-1][0]+RGB[r][c], RGB[r-1][2]+RGB[r][c])

#             else:
#                 RGB[r][c] = min(RGB[r-1][0]+RGB[r][c], RGB[r-1][1]+RGB[r][c])

#     return min(RGB[N-1])
# print(solution())

'''
첫번째풀이- 단순 구현 틀림
'''
# def solution():
#     RGB = []
#     N = int(input())

#     for _ in range(N):
#         RGB.append(list(map(int, input().split())))
    
#     RGB[0] = (min(RGB[0]), RGB[0].index(min(RGB[0])))
    
#     for i in range(1,N):
#         minVal = int(1e9)
#         minIdx = 0

#         for j in range(len(RGB[i])):
            
#             if j != RGB[i-1][1] and RGB[i][j]< minVal:
#                 minVal = RGB[i][j]
#                 minIdx = j

#         RGB[i] = (RGB[i-1][0]+minVal, minIdx)
#     print(RGB)
#     return RGB[N-1][0]
# print(solution())