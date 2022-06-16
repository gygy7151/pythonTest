'''
영화감독 숌
'''
nums =['666']
num = 666
N = int(input())
if N == 1:
    print(nums[0])
else:
    while len(nums) <= N:
        num += 1
        temp_num = list(str(num))
        n = len(temp_num)
        if temp_num.count('6') >= 3:
            for i in range(n):
                if temp_num[i] == '6':
                    if i+1 < n and i+2 < n:
                        if temp_num[i+1] == '6' and temp_num[i+2] =='6':
                            if str(num) not in nums:
                                nums.append(str(num))
    print(nums[N-1])