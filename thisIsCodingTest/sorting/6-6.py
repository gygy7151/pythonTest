'''
계수 정렬
'''

array = [7, 5, 9, 0, 2, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]

lis = [0] * (max(array) + 1)
result = []


for i, el in enumerate(array) :

    print(el, '요소')
    print(i, '인덱스')
    lis[el] += 1

for i, el in enumerate(lis) :

    for _ in range(el) :

        result.append(i) 

print(str(result))

        





