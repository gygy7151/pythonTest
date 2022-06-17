'''
카드2
N장의 카드는 차례로 1부터 N까지의 번호 라벨링
1번카드젤위
N번카드 젤아래위치
카드가 한장 남을때까지 아래과정을 반복
1. 제일위에 있는 카드를 버린다
2. 그다음 제일 위에 있는 카드를 제일 아래에 있는 카드 밑으로 옮긴다
'''
'''
두번째풀이 - 덱 이용
'''
from collections import deque
cards = deque()
N = int(input())

for i in range(1, N+1):
    cards.append(i)

while len(cards) > 1:
    cards.popleft()
    cards.append((cards.popleft()))

print(cards[0])






'''
첫번째풀이 - 시간초과
'''
# N = int(input())
# cards = [str(x) for x in range(1,N+1)]
# print(cards)
# while len(cards) > 1:
#     cards = cards[1:]
#     cards.append(cards[0])
#     cards = cards[1:]
# print(cards[0])

