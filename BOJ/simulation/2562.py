'''
최댓값
'''
answer = int(input())
order = 1

for i in range(2,10):
    num = int(input())
    
    if num > answer:
        answer = num
        order = i

print(answer)
print(order)