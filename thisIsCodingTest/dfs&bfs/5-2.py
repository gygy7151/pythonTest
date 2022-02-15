# 큐예제
# 큐는 선입선출구조
# fist in fist out
# 나중에 온사람이 나중에 나가는 공정한 자료구조임
# 라이브러리 deque 사용하여 큐(Queue)구현함

from collections import deque

queue = deque()

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()


print(queue) 
queue.reverse()
print(queue)
