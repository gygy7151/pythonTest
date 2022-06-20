'''
세번째풀이
'''
def solution(A, K):
    MAX = max(A)
    ans = 10000000001
    for i in range(MAX-1,-1,-1):
        if i in A:
            if ans > (MAX - i):
                ans = (MAX - i)
                return ans
    return ans

# [x for x in range(int(input()))]
A = [5,3,6,1,3]
K = 2
print(solution(A,K))


'''
두번째풀이 -시간초과
'''
# def solution(A, K):
#     N = len(A)
#     start = -1
#     end = K-2
#     ans = 10000000001
#     while True:
#         min_val = 10000000000
#         max_val = -1
#         start += 1
#         end += 1
        
#         if end > N-1:
#             break
#         left = A[0:start]
#         right = A[end+1:]
#         TA = left + right
#         MAX = max(TA)
#         MIN = min(TA)


#         diff = MAX - MIN
#         if diff < ans :
#             ans = diff
#     return ans

# # [x for x in range(int(input()))]
# A = [1] * 100000
# K = 2
# print(solution(A,K))

'''
첫번째 풀이 - 시간초과
'''

# def solution(A, K):
#     N = len(A)
#     start = -1
#     end = K-2
#     ans = 10000000001
#     while True:
#         min_val = 10000000000
#         max_val = -1
#         start += 1
#         end += 1
        
#         if end > N-1:
#             break
#         # print(start,end)
#         for i in range(0,start):
#             # print('i들어감?')
#             # print(i)
#             if A[i] <= min_val:
#                 min_val = A[i]
#             if A[i] >= max_val:
#                 max_val = A[i]
#             # print('-'*50)
#             # print('최댓값, 최솟값')
#             # print(min_val, max_val)
#             # print('-'*50)
#         for j in range(end+1,N):
#             # print(j)
#             if A[j] <= min_val:
#                 min_val = A[j]
#             if A[j] >= max_val:
#                 # print(A[j])
#                 max_val = A[j]
#             # print('-'*50)
#             # print('최댓값, 최솟값')
#             # print(max_val,min_val)
#             # print('-'*50)

#         diff = abs(max_val - min_val)
#         if diff < ans :
#             ans = diff
#     return ans

# # [x for x in range(int(input()))]
# A = [1] * 100000
# K = 2
# print(solution(A,K))