'''
부분수열의 합
'''
'''
첫번째풀이- 재귀함수와 백트래킹
'''
import sys
input = sys.stdin.readline
n, s = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 0

def subset_sum(idx, sub_sum):
    global cnt

    if idx == n: #n보다 크거나 같으면 무조건 종료
        return

    sub_sum += arr[idx]

    if sub_sum == s:
        cnt += 1
    
    # 현재 arr[idx]를 선택한 경우의 가지
    subset_sum(idx+1, sub_sum)

    # 현재 arr[idx]를 선택하지 않은 경우의 가지
    subset_sum(idx+1, sub_sum - arr[idx])

subset_sum(0, 0)
print(cnt)
