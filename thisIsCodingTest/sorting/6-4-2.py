import random
#import sys
#재귀호출 뎁스 확장하는 라이브러리
#sys.setrecursionlimit(10**7)
'''
랜덤하게 피봇추출하여 정렬한 퀵정렬
=> 시간복잡도 가장 낮추는 방법

'''

array  = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]


pivot_idx = round(random.uniform(0, len(array)-1))
pivot = array[pivot_idx]

def first_quick_sort(array, start) :
    
    left = start - 1
    right = start + 1

    while left <= right :

        while left != 0 and left != pivot_idx and array[left] <= pivot:
            left += 1
    
        while right != (len(array) - 1) and right != pivot_idx and array[right] >= pivot :
            right -= 1

        if right == pivot_idx and left == pivot_idx:
            
            break

        else :
            
            array[left], array[right] = array[right], array[left]
    
    second_quick_sort(array, 0, pivot_idx - 1)
    second_quick_sort(array, pivot_idx +1, len(array)- 1)


def second_quick_sort(array, start, end) :

    if start >= end :
        return
    
    pivot = start
    left = start + 1
    right = end

    while left <= right :

        while left <= end and array[left] <= array[pivot] :

            left += 1
        
        while right > start and array[right] >= array[pivot] :

            right -= 1

        
        if left > right :

            array[right], array[pivot] = array[right], array[pivot]
        
        else :

            array[left], array[right] = array[right], array[left]
        
    
    second_quick_sort(array, start, right - 1)
    second_quick_sort(array, right + 1, end)



first_quick_sort(array, pivot_idx)
print(array)
    

