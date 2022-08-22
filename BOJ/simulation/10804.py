'''
카드역배치
'''
'''
첫번째풀이
'''
def solution():
    cards = [ x for x in range(21)]

    for _ in range(10):
        a, b = map(int, input().split())
        cards[a:b+1] = cards[b:a-1:-1]
    
    print(*cards[1:])

solution()
