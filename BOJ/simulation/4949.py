'''
균형잡힌세상
'''
'''
세번째풀이 - 해결
'''
'''
import sys가 아닌 그냥 input()으로 스트링 받는걸로 수정
'''

brackets = {'(': ')', '[': ']'}

def solution():
    ANS = []   

    while True:
        chars = input()
        S = []
        chk = True

        if chars == '.':
            break
        
        for char in chars[0:len(chars)-1]:
            if char in brackets.keys():
                S.append(char)

            elif char in brackets.values():
                if S:
                    if char == brackets[S.pop()]:
                        continue
                chk = False
                break

        if chk and not len(S):
            ANS.append('yes')
        else:
            ANS.append('no')
    return ANS
res = solution()
print(*res, sep="\n")


'''
두번째풀이 - 시간초과 및 틀림
'''
# brackets = {'(': ')', '[': ']'}
# import sys
# input = sys.stdin.readline
# def solution():
#     ANS = []   
#     # print(A)
#     while True:
#         chars = input()
#         S = []
#         chk = True

#         if chars == '.':
#             break
        
#         # 필요없음
#         # if '(' not in chars and '[' not in chars and ')' not in chars and ']' not in chars:
#         #     ANS.append('yes')
#         #     continue
        
#         for char in chars[0:len(chars)-1]:
#             if char in brackets.keys():
#                 S.append(char)

#             elif char in brackets.values():
#                 if S:
#                     if char == brackets[S.pop()]:
#                         continue
#                 chk = False
#                 break

#         if chk:
#             ANS.append('yes')
#         else:
#             ANS.append('no')
#     return ANS
# res = solution()
# print(*res, sep="\n")


'''
첫번째풀이 - 틀림
'''
# import sys

# def solution():
#     A = sys.stdin.readlines
#     A = [ a.rstrip() for a in A()]
#     ANS = []

#     for chars in A:
#         if chars == '.':
#             break
#         S = []
#         prs = True
        
#         for char in chars:
#             # 빈배열일때
#             if not len(S):
#                 if char in ["]", ")"]:
#                     prs = False
#                     break

#                 elif char in ["[", "("]:
#                     S.append(char)

#             else:
#                 if S[-1] in ["[", "("] and char in ["]", ")"]:
#                     S.pop()
                
#                 elif S[-1] in ["]", ")"] and char in ["[", "]", "(", ")"]:
#                     prs = False
#                     break
#         #올바른 문자열인지 판단 및 출력
#         if prs:
#             ANS.append('yes')
#         else:
#             ANS.append('no')

#     return ANS
# print(solution())