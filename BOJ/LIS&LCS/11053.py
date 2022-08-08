'''
최장증가수열 - 연속적이지 않아도 됨
'''
'''
세번째풀이 O(logN), 최장증가수열 자체도 구할 수 있음
'''
from bisect import bisect_left

def solution():
    N = int(input())
    nums = list(map(int, input().split()))

    tmp = [nums[0]]

    for n in nums:
        # 이진탐색해주는 라이브러리
        x = bisect_left(tmp, n)
        
        # tmp에 요소가 없는 경우 bisect tmp길이를 반환한다.
        if x == len(tmp):
            tmp.append(n)

        # 요소가 nums요소가 더 작은 값이 등장하면 오름차순을 위해 tmp에 대입
        elif tmp[x] > n:
            tmp[x] = n
    
    return len(tmp)
print(solution())



'''
두번째풀이 dp활용 5000미만까진 괜찮음 O(N**2)
'''
# def solution():
#     N = int(input())
#     nums = list(map(int, input().split()))

#     dp = [1] * N

#     for n in range(N):  
#         for i in range(n):
#             if nums[i] < nums[n]:
#                 dp[n] = max(dp[n], dp[i]+1)
    
#     return max(dp)
       
# solution()  


'''
첫번째풀이 - 시간 너무 오래걸림 O(2**N)
'''
# N = int(input())
# nums = list(map(int, input().split()))
# lis = [-1] * N
# lis[0] = 1

# # 나(i)를 포함한 가장긴 LIS의 길이 구하기
# for i in range(1,N):
#     i_lis_max_length = 0
#     for j in range(i):
#         if nums[j] < nums[i] and lis[j] > i_lis_max_length:
#             i_lis_max_length = lis[j]    
#     lis[i] = i_lis_max_length + 1

# # LIS 길이들중 가장 큰 값을 출력
# max_lis = lis[0]
# for i in range(1, N):
#     max_lis = max(max_lis, lis[i])
# if max_lis == 0:
#     print(0)
# else:
#     print(max_lis)