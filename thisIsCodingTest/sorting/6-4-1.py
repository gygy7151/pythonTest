'''
호어 퀵정렬
'''
array  = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array, start, end):
    if start >= end :
        return

    pivot = start
    left = start + 1
    right = end

    while left < right :

        if array[start] < array[left] and array[start] > array[right] :
            array[left],  array[right] = array[right], array[left]
        

        if left >= right :

            if left == right :

            if left > right:

    