'''
셀프 넘버

굳이 1부터 10000까지
재귀 돌릴 필요없이
그냥 한번씩만 함수 적용한 값들
리스트에 담아주고
1부터 10000 수들 중에
리스트에 안담긴 애들만 출력하면 간단함
'''
infinity = []

for i in range(1,10001):
    num = list(map(int, str(i)))
    num = sum(num) + i
    infinity.append(num)

for j in range(1,10001):
    if j not in infinity:
        print(j)
