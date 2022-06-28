'''
블랙잭
'''
'''
두번째풀이 
- 더 간단하게 if조건문 누락한것도 해결. 
- 메모리는 첫번째풀이와 동일함
- 시간은 20ms 절약함
'''
# def solution():
#     N, M = map(int, input().split())
#     card = list(map(int, input().split()))
#     return max(card[i]+card[j]+card[k] for i in range(N) for j in range(i) for k in range(j) if card[i]+card[j]+card[k] <= M)
# print(solution())

'''
첫번째풀이 - 카드중복선택 범위 해결 및 split()누락 해결
'''
# def solution():
#     N, M = map(int, input().split())
#     cards = list(map(int, input().split()))
    
#     ans = 0
#     # 카드가 겹치지 않게 선택하려면 N,N,N이 아니라 N,i,j 이런식으로 범위 잡아줘야됨
#     for i in range(N):
#         for j in range(i):
#             for k in range(j):
#                 if (cards[i] + cards[j] + cards[k]) <= M:
#                     ans = max(ans, cards[i] + cards[j] + cards[k])
#     return ans
# print(solution())