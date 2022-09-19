'''
귀찮아 SIB
'''
'''
세번째풀이
'''
def solution():
    N = int(input())
    temp = list(map(int, input().split()))
    nums = [0 for _ in range(N)]
    nums[N-1] = temp[N-1]
    
    # 내림차순으로 담아줘야됨
    for idx in range(N-2, 0, -1):
        nums[idx] = temp[idx] + nums[idx+1]

    
    answer = 0
    
    for idx in range(1, N):
        answer += temp[idx-1]*nums[idx]
    
    print(answer)
solution()

    
    





'''
두번째풀이 - 시간초과
'''
# def solution():
#     N = int(input())
#     num = list(map(int, input().split()))
#     sums = []
    
#     for idx in range(N):
#         sums.append(sum(num[idx:])) # 이건 시간 초과를 발생시킨다
    
#     answer = 0
    
#     for idx in range(1,N):
#         answer += num[idx-1]*sums[idx]
    
#     print(answer)
# solution()
    





# '''
# 첫번째풀이 - 시간초과
# '''
# from itertools import combinations

# def solution():
#     N = int(input())
#     nums = list(map(int, input().split()))
#     answer = 0
    
#     for a, b in combinations(nums, 2):
#         answer += (a + b)
    
#     print(answer)
# solution()
    

    


