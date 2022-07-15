'''
파도반수열
'''
'''
두번째풀이 - 근데 arr구현한거나 연결리스트나 시간 똑같아서 연결리스트가 더 편함
'''
# def solution():
#     ANS = []
#     DP = [0 for _ in range(100)]
#     DP = [1,1,1,2,2,3,4,5,7,9] + [0 for _ in range(91)]

#     for _ in range(int(input())):
#         N = int(input())

#         if N < 10:
#             ANS.append(DP[N-1])
#             continue

#         if DP[N-1] == 0:
#             for i in range(10, N):
#                 if DP[i] == 0:
#                     DP[i] = DP[i-1] + DP[i-5]
            
#         ANS.append(DP[N-1])
    
#     return ANS
# res = solution()
# print(*res, sep="\n")

'''
첫번째풀이
'''
def solution():
    T = int(input())
    ANS = []
    for _ in range(T):
        #DP를 새로운 테스트케이스때마다 초기화 시켜주어야됨
        DP = [1,1,1,2,2,3,4,5,7,9]
        N = int(input())
        if N < 10:
            ANS.append(DP[N-1])
            continue

        # N-1번째 DP요소구해주면됨
        for i in range(10,N):
            DP.append(DP[i-1]+DP[i-5])
        
        ANS.append(DP[N-1])
    
    return ANS
res = solution()
print(*res, sep="\n")