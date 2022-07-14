'''
1,2,3 더하기
'''
'''
두번째풀이
'''
def solution():
    ANS = []

    for _ in range(int(input())):
        N = int(input())
        DP = [0 for _ in range(11)]
        DP[1], DP[2], DP[3] = 1, 2, 4

        if N <= 3:
            ANS.append(DP[N])
            continue

        for i in range(4,N+1):
            # *실수: 연산횟수를 구하는것이 아니므로 +1해줄 필요없음
            DP[i] = sum(DP[i-3:i])
        
        ANS.append(DP[N])
    
    return ANS

res = solution()
print(*res, sep="\n")


'''
첫번째풀이 - 재귀로 접근했더니 뎁스초과
'''
# def iterate(n):
#     if n == 0:
#         return 1

#     iterate(n-1)
#     iterate(n-2)
#     iterate(n-3)

# def solution():
#     ANS = []
#     for _ in range(int(input())):
#         N = int(input())
#         ANS.append(sum(iterate(N)))
#     return ANS
# res = solution()
# print(*res, sep='\n')


