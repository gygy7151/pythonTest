'''
Fly me to the Alpha Centauri
'''
'''
네번째풀이 - 숫자가 대칭을 이루면 또 다른 대칭을 만들기 위해 새로운 수를 추가한다는 것.
참조: https://animoto1.tistory.com/entry/%EB%B0%B1%EC%A4%80-1011-Fly-me-to-the-Alpha-Centauri-%ED%8C%8C%EC%9D%B4%EC%8D%AC-Python
이때 끊은 수를 n이라 하면

 (1) d가 n**2과 같으면 횟수가 n*2-1

 (2) d가 n**2 보다 크고 n**2+n보다 작으면 n*2

 (3) d가 n**2 + n보다 크고 (n+1)**2보다 작으면 n*2+1
'''
import math

def solution():
    T = int(input())
    for _ in range(T):
        x, y = map(int, input().split())
        d = y - x
        num = 1 #최소횟수

        while True:
            if num ** 2 <= d < (num + 1) ** 2:
                break
            else:
                num += 1
        
        if num ** 2 == d:
            print((num*2)-1)
        
        elif num ** 2 < d <= num**2 + num:
            print(num*2)

        else:
            print((num*2)+1)

solution()
'''
세번째풀이-탑다운,dfs형,백트래킹으로 접근함 50%에서 메모리초과 대신 틀렸다는 성과를 얻음
'''
def solution():
    for _ in range(int(input())):
        x, y = map(int, input().split())
        INF = int(1e9)
        dp = [INF,INF,INF]

        def dfs(n,min_cnt): #y-1로시작함
            if n < 0:
                return
            
            if dp[0][0] > min_cnt+1:
                dp[0][0] = min_cnt+1
                dfs(n//2, min_cnt+1)
            if dp[0][1] > min_cnt+1:
                dp[0][1] = min_cnt+1
                dfs(n//2+1,min_cnt+1)
            if dp[0][2] > min_cnt+1:
                dfs(n//2-1,min_cnt+1)

        print(min(dp) + 1)

solution()
            


'''
첫번째/두번째풀이- 메모리초과
'''
# def solution():
#     for _ in range(int(input())):
#         x, y = map(int, input().split())
#         INF = int(1e9)
#         dp = [INF for _ in range(y-x+1)]
#         dp[0] = 0

#         for i in range(1,y-x):
#             dist = dp[i] + 1
#             if 2*i-1 < y-x and dist < dp[2*i-1]:
#                 dp[2*i-1] = dist

#             if 2*i < y-x and dist < dp[2*i]:
#                 dp[2*i] = dist

#             if 2*i+1 < y-x and dist < dp[2*i+1] :
#                 dp[2*i+1] = dist
        
#         print(dp[y-x-1]+1)

# solution()
