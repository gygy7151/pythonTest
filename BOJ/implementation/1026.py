'''
보물
'''
'''
첫번째풀이
'''
def solution():
    N = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    a.sort()
    answer = 0
    for i in range(N):
        answer += a[i]* b.pop(b.index(max(b)))
    
    print(answer)
solution()