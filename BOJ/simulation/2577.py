'''
숫자의 개수
'''
num = 1
for i in range(3):
    num *= int(input())
num = list(str(num))
memo = [0] * 10
for digit in num:
    memo[int(digit)] += 1
for i in range(0, 10):
    print(memo[i])