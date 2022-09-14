'''
1로 만들기
'''
'''
네번째풀이 - bfs 풀이 탑다운방식
'''
from collections import deque
def solution():
    N = int(input())
    dp = [ -1 for _ in range(1000001)]
    dp[N] = 0
    q = deque()
    q.append(N)

    while q:
        num = q.popleft()
        if num == 1:
            break
        
        if num % 3 == 0 and dp[num//3] == -1:
            dp[num//3] = dp[num] + 1
            q.append(num // 3)
        
        if num % 2 == 0 and dp[num//2] == -1:
            dp[num//2] = dp[num] + 1
            q.append(num // 2)
        
        if num - 1 >= 0 and dp[num - 1] == -1:
            dp[num -1] = dp[num] + 1
            q.append(num - 1)
    
    print(dp[1])

solution()




'''
네번째풀이 - bfs - 바텀업방식 메모리초과
'''
# from collections import deque
# def solution():
#     N = int(input())
#     dp = [ -1 for _ in range(1000001) ]
#     dp[1] = 0
#     q = deque()
#     q.append(1)

#     while q:
#         num = q.popleft()
#         if num == N:
#             print(dp[num])
#             return 
#         if num* 3 < 1000000:
#             dp[num* 3] = dp[num] + 1
#             q.append(num*3)
#         if num* 2 < 1000000:
#             dp[num* 2] = dp[num] + 1
#             q.append(num*2)
#         if num +1  < 1000000:
#             dp[num + 1] = dp[num] + 1
#             q.append(num+1)

# solution()

            




'''
세번째풀이 - 초기값을 0으로 설정
'''
# def solution():
#     N = int(input())
#     DP = [0 for _ in range(N+1)]

#     for i in range(2, N+1):

#         # i-1한값으로 초기화
#         DP[i] = DP[i-1] + 1

#         if i % 3 == 0:
#             DP[i] = min(DP[i//3]+1, DP[i])

#         if i % 2 == 0:
#             DP[i] = min(DP[i//2]+1, DP[i])
        
#     return DP[N]
# print(solution())
        
'''
첫번째/두번째풀이 - 초기값을 매우 큰수로 설정한 풀이
'''
# def solution():
#     N = int(input())
#     DP = [int(1e9) for _ in range(N+1)]
#     # print(DP)
#     if N == 2 or N == 3 or N == 5:
#         return 1
#     elif N == 1:
#         return 0
#     else:
#         DP[2], DP[3] = 1, 1

#     for i in range(4, N+1):

#         if i % 5 == 0:
#             DP[i] = min(DP[i//5] + 1, DP[i])

#         if i % 3 == 0:
#             DP[i] = min(DP[i//3] + 1, DP[i])

#         if i % 2 == 0:
#             DP[i] = min(DP[i//2] + 1, DP[i])

#         DP[i] = min(DP[i-1] + 1,DP[i])
#     # print(DP)
#     return DP[i]

# print(solution())