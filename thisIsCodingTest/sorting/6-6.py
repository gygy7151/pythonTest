'''
계수 정렬
'''

array = [7, 5, 9, 0, 2, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]

lis = [0] * (max(array) + 1)
result = []

# 시간 복잡도 O(N)
for i, el in enumerate(array) :

    print(el, '요소')
    print(i, '인덱스')
    lis[el] += 1

# 시간 복잡도 O(i)
for i, el in enumerate(lis) :

    for _ in range(el) :

        result.append(i) 

print(str(result))
# 총 T(n)은 O(N+i)

        





