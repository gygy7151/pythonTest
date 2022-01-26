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