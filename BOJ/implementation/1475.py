'''
방번호
'''
'''
두번째풀이
'''
def solution():
    N = input()
    memo = [0  for _ in range(10)]

    for num in N:
        if int(num) == 6:
            if memo[6] < memo[9]:
                memo[6] += 1
            else:
                memo[9] += 1

        elif int(num) == 9:
            if memo[9] < memo[6]:
                memo[9] += 1
            else:
                memo[6] += 1
        
        else:
            memo[int(num)] += 1

    print(max(memo))
solution()


'''
첫번째풀이 - 틀림
'''
# def solution():
#     N = list(map(int, input()))
#     # 1로 채웠어야했고 0부터 9까지 채웠어야 했는데 단순히 주어진 숫자길이만큼 0으로 채우는 실수를 함..
#     memo = [1 for _ in range(10)]
#     count = 1
    
#     for i in range(len(N)):
#         if N[i] == 6:
            
#             if memo[6] == 0 and memo[9] == 0:
#                 #6을 0으로 바꾸는 실수를 함..
#                 count += 1
#                 memo[9] = 1

#             elif memo[6] == 0 and memo[9] == 1:
#                 memo[9] = 1

#             else:
#                 memo[6] = 0

#         elif N[i] == 9:
#             if memo[9] == 0 and memo[6] == 0:
#                 #6을 0으로 바꾸는 실수를 함..
#                 count += 1
#                 memo[6] = 1

#             elif memo[9] == 0 and memo[6] == 1:
#                 memo[6] = 0

#             else:
#                 memo[9] = 0
        
#         else:

#             if memo[N[i]] == 0:
#                 count += 1

#             else:
#                 memo[N[i]] = 0

#     print(count)

# solution()

