'''
1로 만들기
연산 사용하는 횟수의 최솟값은?
'''

        
x = int(input())

d = [0] * 30001

for i in range(2, x+1) :
    
    print(d)
    d[i] = d[i - 1] + 1

    if i % 2 == 0 :

        d[i] = min(d[i], d[i//2] + 1)

    if i % 3 == 0 :

        d[i] = min(d[i], d[i//3] + 1)
    
    if i % 5 == 0 :

        d[i] = min(d[i], d[i//5] + 1)


print(d[x])
