'''
별 찍기 - 1 
'''
N = int(input())
for i in range(1, N + 1):
    res = ' '*(N-i) +'*'*i +'*'*i +' '*(N-i)
    if i == 1:
        print(' '*(N-i) +'*')
    print(res)
