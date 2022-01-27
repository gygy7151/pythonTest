'''
효율적인 화폐구성
n개의 화페를 최소한 활용해 m원을 만드는게 가장 큰문제
작은 문제는? 
그때 기억나? 연산 4가지
5,3,2로 나누어떨어지면 카운트 추가되고
근데 나누어떨어지는 몫이 최소한 작은걸 골랐잖쓰
안 나누어 떨어지면 -1 햇고
'''

n, m = map(int, input().split())
coins = [0]

for i in range(n) :

    coins.append(int(input()))

print(coins)

res =  [0] * (n+1)
res[1] = (m // coins[1])

for i in range(2, n+1):

    if m % coins[i] == 0 :

        res[i], res[i-1] = min((m // coins[i]), res[i-1]), res[i]


if res[n] == 0 :

    print(-1)

else :

    print(res[n])

    

    