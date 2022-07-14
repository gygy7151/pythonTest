'''
좌표압축
'''
'''
네번째풀이 - 더 쉽고 간단한 풀이
어차피 중복을 제거한 SORTED_X를 기준으로 0번째요소는 제일작은요소이므로 값이 0이되고
즉 인덱스만큼 큰 갯수를 갖는다는걸 알게 된다. 이걸 파악하면 문제가 쉬워짐
1번째요소는 왼쪽에 본인보다 작은요소가 1개 있음을 의미함.
'''

def solution():
    N = int(input())
    X = list(map(int, input().split()))
    SORTED_X = sorted(set(X))
    D = { x: idx for idx, x in enumerate(SORTED_X)}
    return ' '.join(map(str, [D[x] for x in X]))
print(solution())

'''
세번째풀이 - 맞음. 딕서녀리 활용하여 idx 찾는 시간복잡도를 n^2에서 1로 낮춤
'''
def solution():
    N = int(input())
    X = list(map(int, input().split()))
    NX = sorted(list(set(X)), reverse=True)
    D = { val:idx for idx, val in enumerate(NX)}
            
    for x in X:
        idx = D[x]
        print(len(NX)-idx-1 ,end=' ')
    
    print()
    
solution()

'''
두번째풀이 - 딕셔너리와 이분탐색을 활용하면 시간초과해결가능하다고..하는데 잘 모르겟고.. 틀림
'''
def solution():
    N = int(input())
    X = list(map(int, input().split()))
    NX = sorted(list(set(X)), reverse=True)
    
    for x in X:
        print(len(NX)-NX.index(x)-1 ,end=' ')
    
    print()
    
solution()


'''
첫번째풀이 - 시간초과
'''
def solution():
    N = int(input())
    X = list(map(int, input().split()))
    MEMO = [0] * N
    NX = set(X)

    for idx, val in enumerate(X):
        for x in NX:
            if val > x:
                MEMO[idx] += 1
    
    return MEMO
res= solution()
print(*res, sep=' ')