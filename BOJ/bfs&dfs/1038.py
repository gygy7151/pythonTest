'''
감소하는 수
'''
'''
세번째풀이 - 재귀 사용-틀림
'''
# import sys
# input =sys.stdin.readline
# from itertools import combinations

# def solution():
#     N = int(input())
#     answer = []

#     def dfs(num):
#         answer.append(num)
        
#         peak = int(str(num)[0])
#         for i in range(peak + 1, 10):
#             dfs(int(str(i) + str(num)))
        
#     for i in range(10):
#         dfs(i)
    
#     answer.sort()

#     try:
#         print(answer(N))
    
#     except:
#         print(-1)
# solution()

'''
두번째풀이 - brute방식이네 -  조합활용
N은 100만까지이므로
0~9로 1개~10개까지 조합만들고
해당 조합을 감소하는 수로 변경해서 nums에 다 때려박아넣음
그리고 nums[n]구하기ㅋㅋㅋㅋ
'''
import sys
from itertools import combinations

def solution():
    n = int(input())
    nums = []
    
    for i in range(1, 11):
        # 0부터 9까지 구해주어야됨
        for comb in combinations(range(0,10), i):
            #print(comb) comb는 튜플에 담김 주의!
            comb = list(comb)
            comb.sort(reverse=True)
            nums.append(int("".join(map(str, comb))))

    nums.sort()

    try:
        print(nums[n])
    
    except:
        print(-1)
solution()



'''
첫번째풀이 - 31%에서 틀림..
'''
# def solution():
#     N = int(input())
#     MAX = 2000000
#     D = [0,1]

#     def check(num):
#         S = str(num)
#         M = len(S)
#         for idx in range(M-1):
#             # 이렇게 로직을 짜면 32221은 감소하는 수임에도 체크가 안됨
#             if int(S[idx]) > int(S[idx+1]):
#                 continue
#             else:
#                 return False

#         return True

#     order = 1 #1번째가 디폴트
#     for i in range(2,MAX+1):
#         if check(i):
#             D.append(i)
    
#     try:
#         print(D[N])
#     except:
#         print(-1)

# solution()
        
    