'''
1~100의 번호가 쓰인 
카드가 순서대로 나열.
n번째카드부터 n-1장 간격으로
인덱스는 n + n임
카드를 뒤집는 작업을
뒤집는 카드가 더는 없을때가지 계속하자.
'''
n = 100
arr = [False] * n

for i in range(2, n+1) :

    j = i - 1

    while j < len(arr) :

        arr[j] = not arr[j]

        j += i

# 출력하는 부분
for i in range(0, n) :

    if not arr(i) :
        
        print(i + 1)




print(arr)