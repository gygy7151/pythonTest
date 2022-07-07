'''
통계학
'''
'''
두번째풀이
'''
import sys
from collections import Counter
input = sys.stdin.readline

def solution():
    N = int(input())
    S = []
    
    for _ in range(N):
        S.append(int(input()))
    
    S.sort()

    ONE = round(sum(S)/N) if sum(S)/N != 1.5 else 1
    TWO, FOUR = S[int(N/2)], S[-1]-S[0]
    
    THREE = 0
    NS = Counter(S).most_common()

    if len(NS) == 1:
        THREE = NS[0][0]
    
    # NS의 길이가 2이상인경우
    # [0][*]: NS인덱스, [*][0]:주어진 정수들 중 하나, [*][1]:빈도수
    
    # 최빈값이 같은 경우 최빈값중 두번째로 작은값 출력
    # 맨첫번째요소와 그다음번재 즉 두번째요소만 비교해주면 됨
    elif NS[0][1] == NS[1][1]:
        THREE = NS[1][0]
    
    else:
        THREE = NS[0][0]
    
    ANS = [ONE, TWO, THREE, FOUR]
    return ANS
res = solution()
print(*res, sep='\n')

'''
첫번째풀이 - 최빈값 구하는 부부관과 산술평균구하는 부분이 틀렸다.
'''
# import sys
# from collections import Counter
# input = sys.stdin.readline

# def solution():

#     N = int(input())
#     SS = []

#     for _ in range(N):
#         num = int(input())
#         SS.append(num)
    
#     SS.sort()
#     S = Counter(SS) # Counter객체로 감싸져있어서 리스트가 아님
#     MAX = []
#     # print(SS)
#     MAX_COMMON = sorted(S.most_common(), key= lambda x:(-x[1], x[0]) ) # 1번째객체를 반환해달라는 건줄알았는데 객체갯수를 의미하는거였음        
#     # print(MAX_COMMON)
    
#     # 중복되는 요소값도 모두 포함하기 위해 val, 즉 빈도수도 함께 곱해줘야된다.
#     MAX.sort()
    
#     #1 산술평균
#     ## //가 아니라 /고 소수점첫째자리에서 반올림하도록 round로 감싸야됨
#     one = round(sum(SS) / N)
#     #2 중앙값
#     two = SS[N//2]

#     #3 최빈값
#     # 최빈값은 최빈값을 갖는 수를 반환해야함)
#     # 수, 빈도수
#     if len(MAX_COMMON) >= 2:
#         three = MAX_COMMON[1][0]
#     else:
#         three = MAX_COMMON[0][0]

#     #4 범위
#     four = SS[-1] - SS[0]
    
#     return [one, two, three, four] 

# res = solution()
# print(*res, sep='\n')
