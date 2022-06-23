'''
A+B - format은 그냥 출력 안되므로 반드시 print로 출력해줘야됨
'''
for i in range(1,int(input())+1):
    A, B = map(int, input().split())
    C = A + B
    print('Case #{0}: {1} + {2} = {3}'.format(i,A,B,C))