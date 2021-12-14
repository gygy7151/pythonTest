import numpy as np

arr = []
answer = False
count = 0
def solution(input) :
    global answer
    global count
    
    while input != None :
        arr.append(input)
    k = arr[len(arr)-1]
    
    for i in range(len(arr) - k) :
    
        for j in range(i, i-1+k) :

            if arr[j-1] < arr[j] :
                answer = True

            elif arr[j-1] > arr[j] :
                answer = False
        
        if answer == True:
            count = count + 1

    if len(arr) == k:
        count = 1
        return count
    
    else :
        return count

if __name__ == '__main__':
    solution(input)

# 런타임에러뜸