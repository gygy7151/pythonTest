'''
스택수열
'''
'''
세번째풀이 - 로직 개선
'''
N = int(input())
nums = []

for _ in range(N):
    nums.append(int(input()))
ans = []
stack = []
new_stack = []
j = 0

for i in range(1,N+1):
    stack.append(i)
    ans.append('+')
    while stack:
        if stack[-1] == nums[j]:
            j += 1
            res = stack.pop()
            new_stack.append(res)
            ans.append('-')
        else:
            break
if new_stack != nums:
    print('NO')
else:
    for i in range(len(ans)):
        print(ans[i])
        
    
    

'''
두번째풀이 - 틀림
'''
# N = int(input())
# nums = []
# stack = []
# new_stack = []
# ans = []
# j = 0

# for _ in range(N):
#     nums.append(int(input()))

# for i in range(1,N+1):
#     if stack:
#         stack.append(i)
#         ans.append('+')
#         if stack[-1] != nums[j]:
#             continue
#         while stack[-1] == nums[j]:
#             j += 1
#             new_stack.append(stack.pop())
#             ans.append('-')
#             if not stack:
#                 break

# print(nums)
# print(new_stack)
# if new_stack != nums:
#     print('NO')
# else:
#     for i in range(len(ans)):
#         print(ans[i])


'''
첫번째풀이 - 답이 이상함
'''
# N = int(input())
# nums = []
# new_nums = []
# new_stack =[]
# ans = ['+']

# for _ in range(N):
#     nums.append(int(input()))

# stack = [1] + [0]* N
# for i in range(2,N+1):
#     if stack:
#         print(nums)
#         print(stack)
#         if stack[i] != nums[0]:
#             print('같다')
#             stack.append(i)
#             ans.append('+')
#         else:
#             print('다르다')
#             new_nums.append(nums.pop(0))
#             new_stack.append(stack.pop())
#             ans.append('-')

# if new_nums != new_stack:
#     print('NO')
# else:
#     for i in range(len(ans)):
#         print(ans[i])
# print(new_nums)
# print(new_stack)
