'''
나무자르기
'''
'''
두번째풀이 -  이분탐색으로 접근
'''
def solution():
    N, M = map(int, input().split())
    T = list(map(int, input().split()))

    start = 0
    end = max(T)

    while start <= end:

        mid = (start + end) // 2
        sum = 0
        
        for t in T:
            if mid <= t:
                sum += t - mid

        if sum > M:
            start = mid + 1
        
        elif sum < M:
            end = mid - 1

        else:
            end = mid
            break

    return end

print(solution())

'''
첫번째풀이 - 이번엔 시간초과
'''
# import sys
# input = sys.stdin.readline

# def solution():
#     N, M = map(int, input().split())
#     # TH : Tree Height약자
#     TH = list(map(int, input().split()))
#     MAX_TH, MIN_TH = max(TH), min(TH)
#     ANS = 0


#     for H in range(MAX_TH, MIN_TH, -1):
#         L = 0
        
#         for A in TH:
#             # continue 사용조심..
#             if A % H != 0 or A % H != A:
#                 L += (A % H)
        
#         if L == M:
#             ANS = H
#             break

#     return H
# print(solution())
        

            

