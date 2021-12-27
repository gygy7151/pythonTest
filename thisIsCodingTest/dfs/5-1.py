# 자료구조란 '테이터를 표현,관리,처리하기 위한 구조'
#스택예제
#스택은 선입후출구조
#fist in last out

stack  = []

stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()

print(stack) #최하단 원소부터 출력
print(stack[::-1]) #최상단 원소부터 출력
