'''
부품찾기

손님이 요청한 부품 번호의 순서대로 부품을 확인해
부품이 있으면 yes, 없으면 no를 출력한다 구분은 공백으로
데이터 천만이하
'''

n = int(input())
goods = list(map(int, input().split()))
m = int(input())
invoice = list(map(int, input().split()))

goods.sort()

def binary_search(arr, target, start, end) :

    if start > end :

        return

    mid = ( start + end ) // 2

    if arr[mid] == target :

        return True
    
    elif arr[mid] > target :

        return binary_search(arr, target, start, mid -1)
    
    else :

        return binary_search(arr, target, mid + 1, end)


for target in invoice :

    res = binary_search(goods, target, 0, n - 1)

    if res :

        print('yes', end =' ')
    
    else :

        print('no', end =' ')


