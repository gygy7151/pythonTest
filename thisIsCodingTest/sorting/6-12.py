'''
두 배열의 원소 교체
'''
from abc import abstractproperty


n, k = map(int, input().split())
arrA = list(map(int, input().split()))
arrB = list(map(int, input().split()))

arrA.sort()
print(arrA, '오름차순정렬완료')
arrB.sort(reverse=True)
print(arrB, '내림차순정렬완료')

for i in range(k) :

    arrA[i], arrB[i] = arrB[i], arrA[i]

result = sum(arrA)
print(result)
