'''
A+B
'''
for i in range(1,int(input())+1):
    A, B = map(int, input().split())
    C = A + B
    print('Case #{0}: {1} + {2} = {3}'.format(i,A,B,C))