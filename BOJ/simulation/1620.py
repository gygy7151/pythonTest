'''
나는야포켓몬마스터이다솜
'''
'''
첫번째풀이
'''
import sys
input = sys.stdin.readline
def solution():
    N,M = map(int, input().split())
    
    PKM_NAMES = {}#이름->숫자 
    #숫자는 1부터시작함으로 0번째는 None
    PKM_NUM = ['None']#숫자->이름

    for i in range(N):
        PKM_NAME = input().rstrip()
        PKM_NUM.append(PKM_NAME)
        #숫자는 1부터인데 i는 0부터 시작하므로 +1
        PKM_NAMES[PKM_NAME] = i+1
    #Q: 숫자-> 이름출력 이름->숫자출력
    for _ in range(M):
        Q = input().rstrip()
        try:
            if PKM_NUM[int(Q)]:
                print(PKM_NUM[int(Q)])
        except:
            print(PKM_NAMES[Q])

solution()