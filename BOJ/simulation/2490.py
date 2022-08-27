'''
부분수열의 합
'''
'''
첫번째풀이- 재귀함수와 백트래킹
'''
def solution():
    for _ in range(3):
        maps = list(map(int, input().split()))
        zero, one = maps.count(0), maps.count(1)
        
        if zero == 1 and one == 3:
            print('A')
        elif zero == 2 and one == 2:
            print('B')
        
        elif zero == 3 and one == 1:
            print('C')
        
        elif zero == 4:
            print('D')
        elif one == 4:
            print('E')

solution()