'''
위에서 아래로
하나의 수열에는 다양한 수가 존재한다.
이러한 수는 크기에 상관없이 나열되어 있다.
이수를 큰수부터 작은 수의 순서로 정렬해야 한다.
내림차순으로 정렬하는 프로그램을 만드시오

[입력조건]
첫째줄에 수열에 속해있는 수의 개수 N이 주어진다.
둘째줄 부터 N+1 번째 줄까지 N개의 수가 입력딘다. 1이상 10만이하의 자연수 이다.

아 한줄에 여러개 숫자가 있을 땐
map(int, input().split()) 이런거 활용하면 됨..

[출력조건]
내림차순으로 공백으로 구분하여 출력한다
동일한 수의 순서는 자유롭게 가능

'''
import random

n = int(input())
arr = []

for i in range(n) :
    
   arr.append(int(input()))

pivot_idx = random.randint(0, n-1)
arr[pivot_idx], arr[0] = arr[0], arr[pivot_idx]

def quick_sort(arr, start, end) :

    if start >= end :
        return

    pivot = start
    left = start + 1
    right = end

    while left <= right :

        while left <= end and arr[left] > arr[pivot] :

            left += 1

        while right > start and arr[right] < arr[pivot] :

            right -= 1
        
        if left > right :

            arr[right], arr[pivot] = arr[pivot], arr[right]

        else :

            arr[right], arr[left] = arr[left], arr[right]
        
        quick_sort(arr, start, right - 1)
        quick_sort(arr, right + 1 , end)
    
quick_sort(arr, 0, n-1)
print(arr)