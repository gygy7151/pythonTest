'''
야구공 - 17281번
'''
'''
두번째 풀이 - 훨씬간단하다
'''
from itertools import permutations

n = int(input())
p = list(permutations([x for x in range(1, 9)], 8))
board = [list(map(int, input().split(' '))) for x in range(n)]
answer = 0

for i in set(p):
    order = list(i[:3]) + [0] + list(i[3:])
    score = 0
    index = 0
    for inning in range(n):
        out = 0
        base1, base2, base3 = 0, 0, 0
        while out != 3:
            if board[inning][order[index]] == 0:
                out += 1
            elif board[inning][order[index]] == 1:
                score += base3
                base1, base2, base3 = 1, base1, base2
            elif board[inning][order[index]] == 2:
                score += (base2 + base3)
                base1, base2, base3 = 0, 1, base1
            elif board[inning][order[index]] == 3:
                score += (base1 + base2 + base3)
                base1, base2, base3 = 0, 0, 1
            elif board[inning][order[index]] == 4:
                score += (base1 + base2 + base3 + 1)
                base1, base2, base3 = 0, 0, 0
            index += 1
            if index == 9:
                index = 0

    answer = max(answer, score)
print(answer)
'''
첫번째풀이 - 시간초과
'''
# import itertools
# import copy

# def fulfill(roo, num):
#     for i in range(num-1):
#         roo.append(0)
#     return roo
# def ining(order,times,score):
#     if times == N:
#         return
#     global px
#     global max_score
#     out = 0
#     end = []
#     roo = [0,0,0]
#     start = copy.deepcopy(order)
#     while out < 3:
#         for p_num in order:
#             if len(start) == 0:
#                 start = copy.deepcopy(end)
#             if px[times-1][p_num-1] == 0:
#                 end.append(start.pop(0))
#                 out += 1

#             elif px[times-1][p_num-1] == 1:
#                 starter = start.pop(0)
#                 roo.append(starter)
#                 striker = roo.pop(0)
#                 if striker != 0:
#                     score += 1
#                     end.append(striker)
            
#             elif px[times-1][p_num-1] == 2:
#                 starter = start.pop(0)
#                 roo.append(starter)
#                 striker = roo.pop(0)
#                 if striker != 0:
#                     score += 1
#                     end.append(striker)
#                 roo = fulfill(roo, 2)
#                 for _ in range(1):
#                     striker = roo.pop(0)
#                     if striker != 0:
#                         score += 1
#                         end.append(striker)
#             elif px[times-1][p_num-1] == 3:
#                 starter = start.pop(0)
#                 roo.append(starter)
#                 striker = roo.pop(0)
#                 if striker != 0:
#                     score += 1
#                     end.append(striker)
#                 roo = fulfill(roo, 3)
#                 for _ in range(2):
#                     striker = roo.pop(0)
#                     if striker != 0:
#                         score += 1
#                         end.append(striker)
#             else:
#                 starter = start.pop(0)
#                 roo.append(starter)
#                 striker = roo.pop(0)
#                 if striker != 0:
#                     score += 1
#                     end.append(striker)
#                 roo = fulfill(roo, 4)
#                 for _ in range(3):
#                     striker = roo.pop(0)
#                     if striker != 0:
#                         score += 1
#                         end.append(striker)
#     new = start + end
#     ining(new, times+1, score)
#     max_score = max(max_score, score)
#     return

# max_score = 0
# player = [x for x in range(2,10)]
# player = list(itertools.permutations(player))
# for id, lis in enumerate(player):
#     arr = list(lis)
#     arr.insert(3, 1)
#     player[id] = arr

# N = int(input())
# px = [list(map(int, input().split())) for _ in range(N)]
# for order in player:
#     #순번, 몇회차, 점수
#     ining(order, 0, 0)

# print(max_score)