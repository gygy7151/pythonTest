# 재귀함수는 가장 마지막에 호출한 함수가 먼저 수행을 끝내야 그 앞의 함수 호출이 종료되므로 스택자료구조를 이용한다.

# 반복적으로 구현한 n!
def factorial_iterative(n) :
    result = 1

    # 1부터 n까지의 수를 차례대로 곱하기
    for i in range(1, n+1) :
        result *= i
    return result

# 재귀적으로 구현한 n!
def factorial_recursive(n) :
    if n <= 1 :
        return 1
    
    return n * factorial_recursive(n-1)

result = factorial_iterative(10)
print(result)

