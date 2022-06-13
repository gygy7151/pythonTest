'''
X보다 작은수
'''
N, X = map(int, input().split())
nums = list(map(int, input().split()))
ans = []
for i in range(N):
    if nums[i] < X:
        ans.append(nums[i])
print(*ans)