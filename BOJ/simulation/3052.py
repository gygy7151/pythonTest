'''
나머지
'''
nums = []
for i in range(10):
    n = int(input())
    n = n % 42
    if n not in nums:
        nums.append(n)
print(len(nums))