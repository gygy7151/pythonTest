'''
평균
M = 최댓값
모든점수를 점수/M * 100
'''
N = int(input())
nums = list(map(int, input().split()))
max_num = max(nums)
ans = 0
for i in range(N):
    nums[i] = (nums[i] / max_num) * 100
    ans += nums[i]
ans /= N
print(ans)
