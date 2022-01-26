'''
개미전사

문제가 뭐야?

'''
n =  int(input())
stores = list(map(int, input().split()))

for i in range(3, n, 2) :

    stores[i] += stores[i-2]

for i in range(2, n, 2) :

    stores[i] += stores[i-2]

if stores[n-1] > stores[n-2] :

    print(stores[n-1])

else :
    print(stores[n-2])


'''
print(max(d[n-1], d[n-2]))

근데 굳이 위와 같이 안나누고 더 빨리 하는 방법 있음

d = [0] * 100

d[0] = stores[0] 
d[1] = max(stores[0], stores[1])

for i in range(2, n) :

    d[i] = max(d[i-1], d[i-2] + stores[i])

print(d[n-1])
'''