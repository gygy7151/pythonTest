'''
A -> B
'''
'''
세번째풀이
'''
def solution():
    A, B = map(int, input().split())
    cnt = 1
    while A != B:
        cnt += 1
        temp = B

        if B % 2 == 0:
            B //= 2

        elif B % 10 == 1:
            B //= 10

        if temp == B:
            print(-1)
            break        
    else:
        print(cnt)
solution()


'''
두번째풀이 - 틀림. 홀 수인 경우에 2로 나누고 있었고..결론적으로 시간초과남
'''
def solution():
    A, B = map(int, input().split())
    cnt = 1
    while B != A:
        cnt += 1
        
        if B % 10 == 1:
            B-= 1
            
        elif B % 2 == 0:
            B//= 2
        
        if B < 0:
            print(-1)
            break
    else:
        print(cnt)
solution()




'''
첫번째풀이
'''
from collections import deque
def solution():
    A, B = map(int, input().split())

    def multiple(n):
        return n*2
    
    def addOne(n):
        return n*10 + 1
    
    #아 최종적으로 1을 더해줘야되니깐 아예처음부터 1을더해준다
    q = deque([(A,1)])

    while q:
        num, cnt = q.popleft()

        if num == B:
            print(cnt)
            break
        
        if num > B:
            continue
            
        q.append((multiple(num), cnt+1))
        q.append((addOne(num), cnt+1))
    #n이B보다 크면 바로 break가 아니라 q에 넣지않는다.
    #while문을 벗어나면 같은게 아예없다는 의미이므로 -1출력해주면 된다.
    else:
        print(-1)

solution()