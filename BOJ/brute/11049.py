'''
행렬곱셈순서
'''
import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
for _ in range(N-1):
    _, m = map(int, input().split())
    nums.append(m)

DP = [[0] * N  for _ in range(N)]

for choices in range(N):
    for start in range(N-choices):
        end = start + choices
        if start == end:
            continue
        # 0이 디폴트값이므로 최소비교가 불가하므로 임시로 스트링 값을 채워줌
        DP[start][end] = float('inf')
        for mid in range(start, end):
            DP[start][end] = min(DP[start][end], DP[start][mid] + DP[mid+1][end] + (nums[start] * nums[mid+1] * nums[end+1]))
print(DP[0][N-1])