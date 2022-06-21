'''
프린터 큐
''' 
'''
두번째 풀이 deque사용
'''


'''
첫번째풀이 - 리스트 사용
'''
def print_check(priority):
    global print_cnt
    while True:
        # 0번째요소가 중요도, 1번째요소가 idx
        reversed_priority = sorted(priority, key = lambda x: (-x[0]))
        MAX = reversed_priority[0][0]
        # 프린트불가능
        if priority[0][0] < MAX:
            priority.append(priority.pop(0))
            
        # 프린트가능
        else:
            print_cnt += 1
            if priority[0][1] == target_idx:
                print(print_cnt)
                break
            priority.pop(0)

for i in range(int(input())):
    N, target_idx = map(int, input().split())
    priority = list(map(int, input().split()))
    # priority = [ x for x in range(5)] * 20
    
    for i in range(N):
        priority[i] = (priority[i],i)
    print_cnt = 0
    if N == 1:
        print_cnt += 1
        print(print_cnt)
        continue
    
    print_check(priority)



        

            

