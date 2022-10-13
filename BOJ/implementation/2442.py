'''
별찍기 - 5
'''
'''
첫번째풀이
'''
'''
N번째줄에는 별 2*N-1개 찍는 문제
'''
N = int(input())

for i in range(N-1,0,-1):
    ans = ''
    for _ in range(i):
        ans += ' '
    
    for _ in range((N-i)*2-1):
        ans += '*'
    

    print(ans)

print('*'* (2*N-1))








