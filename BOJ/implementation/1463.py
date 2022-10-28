'''
1로 만들기
'''
'''
두번째풀이- 점화식은 이전 결과를 다음 결과에 이용하게 되는 점화식을 활용한 DP 문제이다
아.. 인덱스를 숫자로 활용 인사이트 다시 얻음
'''
def solution():
    N = int(input())
    dp = [0] * (N+1)

    # 애초 0과 1은 연산이 0번이니깐 2부터 계산해준다
    for i in range(2, N+1):
        dp[i] = dp[i-1] + 1

        if i % 2 == 0:
            dp[i] = min(dp[i], dp[i//2]+1)
        
        if i % 3 == 0:
            dp[i] = min(dp[i], dp[i//3]+1)
    
    print(dp[N])

solution()



'''
첫번째풀이 - 틀림

# 1~3번 연산횟수를 저장하는 리스트 count를 선언한다
# N이 1이보다 클때까지 1~3번 연산을 반복하고, 반복한 값을 각 리스트에 저장한다
'''
# from collections import deque

# def solution():
#     N = int(input())
#     cnt = 0
#     res = deque()
#     res.append(N)
    
#     while True:
#         while res:
#             num = res.popleft()
#             if num - 1 > 0:
#                 res.append(N-1)
            
#             if num % 3 == 0 and int(num / 3) > 0:
#                 res.append(int(num/3))
            
#             if num % 2 == 0 and int(num / 2) > 0:
#                 res.append(int(num/2))
        
#         res.sort()
#         print(res)
#         if res[0] != 1:
#             N = res[0]
#             cnt += 1
#         else:
#             print(cnt+1)
#             return
# solution()















        


    
        
# 3개의 연산을 미리 한값중에 가장 작은 값을 구하고 그게 1인지 아닌지 체크하고 1이면 i를 출력해주고
# 1이 아니면 dp[현재인덱스]에 저장해주고 넘어가면 되잖씀??인덱스를 연산 횟수라고 치자
# i는