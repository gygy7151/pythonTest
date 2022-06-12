'''
셀프 넘버


'''
infinity = []

for i in range(1,10001):
    num = list(map(int, str(i)))
    num = sum(num) + i
    infinity.append(num)

for j in range(1,10001):
    if j not in infinity:
        print(j)
