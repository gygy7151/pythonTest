'''
집합
'''
'''
세번째풀이 - DP활용 + 비트마스크에 영감비슷하게 받아 실체는 없애고 실존하는지 여부만 체크
'''
import sys
input = sys.stdin.readline

def solution():
    DP = [0] * 21 #1~20까지위해 +1해줌
    M = int(input())
    #애시당초 처음부터 중복되는거 안들어오도록 막기
    for _ in range(M):
        C = input().split()
        A = C[0]
        try:
            B = int(C[1])
        except:
            pass

        if A == 'add':
            DP[B] = 1

        elif A == 'remove':
            DP[B] = 0

        elif A == 'check':
            if DP[B] == 1:
                print(1)
            else:
                print(0)
        
        elif A == 'toggle':
            if DP[B] == 1:
                DP[B] = 0
            
            else:
                DP[B] = 1

        elif A == "all":
            DP = [0] + [1] * 20
        
        #empty
        else:
            DP = [0] * 21
            #S.clear() # 또는 S.remove() 괄호안에 인자없으면 전체삭제한다
solution()


'''
두번째풀이 - 72%에서 틀림
'''
# import sys
# # 라인별로 입력받도록 수정
# input = sys.stdin.readline
# def solution():
#     S = []
#     NS = { x for x in range(1,21)}
#     M = int(input())

#     for _ in range(M):
#         c = input().split()
#         if len(c) == 2:
#             c[1] = int(c[1])
#             prs = True if c[1] in S else False

#         if 'all' in c[0]:
#             S = NS
#             continue

#         elif 'empty' in c[0]:
#             S = []
#             continue

#         elif 'add' in c[0] and not prs:
#             if type(S) == type({1}):
#                 S.add(c[1])
#                 continue
#             S.append(c[1])

#         elif 'remove' in c[0]:
#             if type(S) == type({1}):
#                 continue
#             if not prs:
#                 continue
#             S.remove(c[1])
        
#         elif 'check' in c[0]:
#             if not prs:
#                 print(0)
#             else:
#                 print(1)

#         elif 'toggle' in c[0]:
#             if not prs:
#                 if type(S) == type({1}):
#                     continue
#                 S.append(c[1])
#             else:
#                 S.remove(c[1])
        
# solution()

'''
첫번째풀이 - 10828 스택문제 참조
'''

# import sys
# # 라인별로 입력받도록 수정
# input = sys.stdin.readline
# def solution():
#     S = []
#     NS = { x for x in range(1,21)}
#     M = int(input())

#     for _ in range(M):
#         c = input().split()
#         print(c)
#         if len(c) == 2:
#             c[1] = int(c[1])
#             prs = True if c[1] in S else False

#         if 'all' in c[0]:
#             S = NS
#             continue

#         elif 'empty' in c[0]:
#             S = []
#             continue

#         elif 'add' in c[0] and not prs:
#             if type(S) == type({1}):
#                 S.add(c[1])
#                 continue
#             S.append(c[1])

#         elif 'remove' in c[0]:
#             if type(S) == type({1}):
#                 continue
#             if not prs:
#                 continue
#             S.remove(c[1])
        
#         elif 'check' in c[0]:
#             if not prs:
#                 print(0)
#                 print(S)
#             else:
#                 print(1)
#                 print(S)

#         elif 'toggle' in c[0]:
#             if not prs:
#                 if type(S) == type({1}):
#                     continue
#                 S.append(c[1])
#             else:
#                 S.remove(c[1])
        
# solution()