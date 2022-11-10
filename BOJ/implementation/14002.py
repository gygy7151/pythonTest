'''
가장 긴 증가하는 부분 수열4
'''
'''
첫번째풀이
'''
def solution():
    N = int(input())
    arr = list(map(int, input().split()))
    dp = [1 for _ in range(N+1)]


    for i in range(N):
        for j in range(i):
            if arr[j] < arr[i]:
                dp[i] = max(dp[i], dp[j]+1)
    
    x = max(dp)

    result = []
    for i in range(N-1, -1, -1):
        if dp[i] == x:
            result.append(arr[i])
            x -= 1
    
    result.reverse()
    for r in result:
        print(r, end=' ')



