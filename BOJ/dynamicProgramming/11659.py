'''
구간합구하기4
'''
'''
두번째풀이
'''
import sys
input = sys.stdin.readline

def solution():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))

    #변수를 활용해 이전값 차근차근더해줄것
    sum_val = 0
    #연결리스트로 접두사합 추가해주고
    P = [0]
    for num in A:
        sum_val += num
        P.append(sum_val)
    
    for _ in range(M):
        left, right = map(int, input().split())
        print(P[right] - P[left-1])

solution()

'''
첫번째풀이 - 시간초과
'''
import sys
input = sys.stdin.readline

def solution():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    
    # 접두사합 저장
    P = [0 for _ in range(N+1)]
    # ***이부분에서 O(NM)으로 상당한 시간초과 발생함
    for i in range(1,N+1):
        P[i] = sum(A[idx] for idx in range(0,i))

    for _ in range(M):
        LEFT, RIGHT = map(int, input().split())
        print(P[RIGHT] - P[LEFT-1])

solution()

