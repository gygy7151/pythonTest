'''
연속합
'''
'''
첫번째풀이
'''
def solution():
    N = int(input())
    arr = list(map(int, input().split()))
    ans = [0 for _ in range(N)]
    ans[0] = arr[0]

    for i in range(1, N):
        ans[i] = max(arr[i], ans[i-1]+arr[i])
    print(max(ans))

solution()