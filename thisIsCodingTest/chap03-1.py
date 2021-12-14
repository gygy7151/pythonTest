'''
당신은 음식점의 계산은 도와주는 점원이다
사용할 500원 100원 50원 10원짜리의 동전이 무한히 존재한다고 가정
동전의 최소개수를 구하라 거슬러줘야할돈 N은 항상 10의배수
'''

n = int(input())
'''
count = 0

coin_types = [500, 100, 50, 10]

for coin in coin_types:
    count += n // coin
    n %= coin

print(count)
'''


'''



'''

def solution(N):
    five_hundred = N // 500
    one_hundred = (N % 500) // 100
    fifthy = ((N % 500)%100) // 50
    ten = (((N % 500)%100)%50) // 10

    count = five_hundred + one_hundred + fifthy + ten

    print(count)

solution(n)
