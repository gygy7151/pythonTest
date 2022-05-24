'''
LIS
'''
N = int(input())
nums = list(map(int, input().split()))
lis = [-1] * N
lis[0] = 1

# 나(i)를 포함한 가장긴 LIS의 길이 구하기
for i in range(1,N):
    i_lis_max_length = 0
    for j in range(i):
        if nums[j] < nums[i] and lis[j] > i_lis_max_length:
            i_lis_max_length = lis[j]    
    lis[i] = i_lis_max_length + 1

# LIS 길이들중 가장 큰 값을 출력
max_lis = lis[0]
for i in range(1, N):
    max_lis = max(max_lis, lis[i])
if max_lis == 0:
    print(0)
else:
    print(max_lis)