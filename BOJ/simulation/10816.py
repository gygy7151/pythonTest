'''
숫자카드2
'''
'''
두번째풀이 - sort를 제외해도 무거워서 이분탐색을 적용
어차피 한번만 쭉돌면서 중복되는 카드 딕셔너리 CNT에 표시만할꺼라
따로 방문했냐 안했냐 표시할 필요 없음
'''
import sys
def solution():
    input = sys.stdin.readline
    N, CARDS = int(input().rstrip()), list(map(int, input().rstrip().split()))
    M, NUMS = int(input().rstrip()), list(map(int, input().rstrip().split()))
    CNT = {}

    # 미리 중복되는 갯수들 구해줌
    for c in CARDS:
        if c not in CNT:
            CNT[c] = 1
        else:
            CNT[c] += 1
    
    ANS = []
    #이분탐색 활용
    for n in NUMS:
        start = 0
        end = N-1
        prs = False

        # 굳이 따로 메소드로 뺄 필요없음 카드 한번만 돌면되서 for문아래 while문임
        while start <= end:
            mid = (start+end)//2
            
            if CARDS[mid] == n:
                ANS.append(CNT[n])    
                prs = True
                break
            
            elif CARDS[mid] > n:
                end = mid - 1

            else:
                start = mid + 1
        # 반드시 표시해줘야됨
        if not prs:        
            ANS.append(0)

    return ANS
res = solution()
print(*res, sep=' ')

'''
첫번째풀이 - 시간초과
'''
'''
N : 상근이가 가지고 있는 숫자카드개수 (1 <= N <= 500,000)
숫자카드에 적힌 수의 범위는 -천만이상 ~ 천만이하임
M : 상근이가 갖고있는지 구해야할 카드 개수
체크해야할 숫자카드에 적힌 수의 범위는 -천만이상 ~ 천만이하임
출력은 한줄에 공백으로 구분함
'''
# import sys
# def solution():
#     #여기서 바로 rstrip()해버리면 값 하나밖에 안들어감
#     input = sys.stdin.readline
#     N, NCARD = int(input().rstrip()), list(map(int, input().rstrip().split()))
#     M, MCARD = int(input().rstrip()), list(map(int, input().rstrip().split()))
#     M_MEMO = [0] * M
#     CNT = {}
#     NCARD.sort()
#     for i in range(M):
#         prs = False
#         for n in NCARD:
#             if MCARD[i]  == n and not M_MEMO[i]:
#                 CNT[MCARD[i]] = 1
#                 M_MEMO[i] = 1
#                 prs = True
#             elif MCARD[i] == n and M_MEMO[i]:
#                 CNT[MCARD[i]] += 1
#         # 없는 경우도 예외처리 해주어야됨
#         if not prs:
#             CNT[MCARD[i]] = 0
#     ANS = [ x for x in CNT.values()]
#     return ANS
# res = solution()
# print(*res, sep=' ')