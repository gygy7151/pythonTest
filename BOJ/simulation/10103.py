'''
주사위게임
'''
'''
첫번째풀이
'''
def solution():
    scoreA = 100
    scoreB = 100
    N = int(input())

    for _  in range(N):
        A, B = map(int, input().split())

        if A > B:
            scoreB -= A

        elif A < B:
            scoreA -= B
    
    print(scoreA, scoreB, sep="\n")
solution()
