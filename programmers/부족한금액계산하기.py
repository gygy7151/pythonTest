'''
부족한금액계산하기
'''
def solution(price,money,count):
    return max(0, money-(((price)*(price+1)*(count))//2))

p,m,c = 10,50,4
print(solution(p,m,c))