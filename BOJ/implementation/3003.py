'''
킹, 퀸, 룩, 비숍, 나이트, 폰
'''
'''
첫번째풀이
'''
def solution():
    #체스의 총개수는 16개
    #몇개를 더하거나 빼야 올바른 세트가 되는지 구해야됨
    basicChaseCnt = [1,1,2,2,2,8]
    nowChaseCnt = list(map(int, input().split()))
    answer = []
    for idx in range(6):
        if basicChaseCnt[idx] > nowChaseCnt[idx] or basicChaseCnt[idx] < nowChaseCnt[idx]:
            answer.append(basicChaseCnt[idx] - nowChaseCnt[idx])

        else:
            answer.append(0)
    
    print(*answer)
solution()

        

        