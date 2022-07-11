'''
ATM
'''
'''
네번째풀이
'''
def solution():
    N = int(input())
    T = list(map(int, input().split()))
    T.sort()

    ANS = 0

    for i in range(1,N+1):
        i_time = sum(T[:i])
        ANS = i_time + ANS

    return ANS

print(solution())

'''
세번째풀이 - 틀림 - 문제에서 요구하는 논리가 아니였음, 그리고 굳이 Counter필요없음
'''
# from collections import Counter
# def solution():
#     N = int(input())
#     T = list(map(int, input().split()))
#     T = Counter(T).most_common()
#     T.sort(key= lambda x: x[0])
    
#     ANS = 0
#     for time, people_num in T:
#         for _ in range(people_num):
#             ANS += (time + ANS)
#     return ANS
# print(solution())
'''
두번째풀이 - DP로 접근하려 햇으나 P[i]값이 일정하지 않아서
'''
# def solution():
#     N = int(input())
#     P = list(map(int, input().split())) 
#     DP = [min(P)] + [0] * N

#     def iterate(n):

#         if n < 0:
#             return
        
#         DP[n] = min(DP[n-1] + P[n+1], DP[n-1])

#         return DP[n]
    




'''
첫번째풀이 - 메모리초과
'''
# from itertools import permutations
# def solution():
#     N = int(input())
#     P = list(map(int, input().split()))
#     WAITNIG_ORD = list(permutations(P, N))
#     P = [0] + P
#     MIN_TIME = int(1e9)
#     # tuple is iterator
#     for ord in WAITNIG_ORD:
#         T = 0
#         for i in range(N):
#             T += ( sum(P[x+1] for x in ord[:i] )+ P[i+1])
        
#         MIN_TIME = min(T, MIN_TIME)
    
#     return MIN_TIME
# print(solution())
