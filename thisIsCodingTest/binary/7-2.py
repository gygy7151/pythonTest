'''
이진탐색구현 - 재귀함수활용
'''

def binary_search(arr, target, start, end) :

    if start >  end :

        return None

    mid = (start + end) // 2

    if arr[mid] == target :

        return mid

    elif arr[mid] > target :

        return binary_search(arr, target, start, mid - 1)
    
    else : 

        return binary_search(arr, target, mid + 1, end)
    

n, target = map(int, input().split())
arr = list(map(int, input().split()))


res = binary_search(arr, target, 0, n-1)
print(res)