'''
이상한 문자 만들기
'''
'''
세번째풀이 - 람다활용
'''
def solution(s):
    return ' '.join(map(lambda x: ''.join([a.lower() if idx % 2 else a.uppper() for idx, a in enumerate(x)]), s.split(" ")))


'''
두번째풀이 - 성공(단, string에 직접접근하지 않도록 주의. 특정값 할당이 안됨)
'''
# def solution(s): 
#     IDX = -1
#     ANS = list(s)
#     for i in range(len(ANS)):
#         if ANS[i] == ' ':
#             IDX = -1
#             continue

#         IDX += 1
#         if IDX % 2 == 0:
#             ANS[i] = ANS[i].upper()
#         else:
#             ANS[i] = ANS[i].lower() 

#     ANS = "".join(ANS)
#     return ANS


'''
첫번째풀이 - 띄어쓰기 공백이 두개이상인 애들부턴 틀림
'''
# def solution(s):
#     S = s.split()
#     ANS = []
#     for w in S:
#         W = ''

#         for i in range(len(w)): 

#             if i % 2 == 0:
#                 W += w[i].upper()

#             else:
#                 W += w[i].lower()

#         ANS.append(W)
#     ANS = " ".join(ANS)
#     if s[-1] == ' ':
#         ANS += ' '
#     return ANS

# print('결과:{}'.format(solution('try    hello    world')))