'''
숫자의합
'''
N = int(input())
nums = str(input())
n_sum = 0
for i in range(N):
    if int(nums[i]) > 0:
        n_sum += int(nums[i])
print(n_sum)