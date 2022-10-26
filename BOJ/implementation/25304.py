'''
영수증
'''
'''
첫번째풀이
'''
def solution():
    # 영수증에 적힌 총 금액X
    X = int(input())
    # 영수증에 적힌 구매한 물건의 종류수 N
    N = int(input())
    total = 0

    for _ in range(N):
        costGoods, cntGoods = map(int, input().split())
        total += (costGoods * cntGoods)

    print('Yes' if X == total else 'No')

solution()