'''
1이 될때까지

어떤 수 N이 1이될때까지 다음의 두과정 중 
하나를 반복적으로 선택하여 수행하려고 한다.
단 두번째 연산은 N이 K로 나누어떨어질대만 선택가능

'''

n, k = map(int, input().split())

def solution(n, k):
    count = 0

    while n >= k :
    #n이 k로 나누어 떨이지는지 확인한다
    #1-나누어 떨어지면 n을 k로 나눈다
        if n % k == 0 :
            n //= k
            count +=  1
    #2-그렇지 않으면 n에서 1을뺀다
        elif n % k != 0 :
            n -= 1
            count +=  1
    
    while n > 1 :
        n -= 1
        count += 1
            
    #1,2 과정을 한번이라도 수행한 경우 count+= 1한다.

    print(count)
    #위 과정을 while문을 반복한다.

solution(n, k)