'''
시계사진들
'''
'''
첫번째풀이 - 틀림
'''
def solution():
    N = int(input())
    parent = set(list(input().split()))
    pattern = set(list(input().split()))


    for time in parent:
        if time in pattern:
            print('possible')
            return

    print('impossible')
    return
solution()


