'''
전자레인지
'''
'''
첫번째풀이
'''
def solution():
    T = int(input())

    if T % 10 != 0:
        print(-1)
        return
    
    timer = [300, 60, 10]
    ans = []

    for time in range(3):
        ans.append( T // timer[time])
        T = T % timer[time]
    
    print(*ans)
solution()


