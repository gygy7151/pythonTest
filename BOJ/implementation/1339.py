'''
단어수학
'''
'''
두번째풀이
'''
import sys

n = int(sys.stdin.readline())

alpha = [] # 단어를 저장할 리스트
alpha_dict = {} # 단어 내의 알파벳별로 수를 저장할 딕셔너리
numList = [] # 수를 저장할 리스트

for i in range(n): # 단어를 입력받음
    alpha.append(sys.stdin.readline().rstrip())

for i in range(n): # 모든 단어에 대해서
    for j in range(len(alpha[i])): # 단어의 길이만큼 실행
        if alpha[i][j] in alpha_dict: # 단어의 알파벳이 이미 dict에 있으면
            alpha_dict[alpha[i][j]] += 10 ** (len(alpha[i])-j-1) # 자리에 맞게 추가 ( 1의 자리면 1 )
        else:   # 자리에 없으면 새로 추가 ( 10의 자리면 10 )
            alpha_dict[alpha[i][j]] = 10 ** (len(alpha[i])-j-1)

for val in alpha_dict.values(): # dict에 저장된 수들을 모두 리스트에 추가
    numList.append(val)

numList.sort(reverse=True) # 수들을 내림차순 정렬

sum = 0
pows = 9
for i in numList: # 첫 번째 부터 가장 큰 부분을 차지하므로 9를 곱해준다
    sum += pows * i
    pows -= 1
# 내려갈수록 그 알파벳이 차지하는 비중이 적으므로 -1 
print(sum)


'''
첫번째풀이 - 그 물에 잠기는 조건을 이상하게 27번줄처럼 생각해서 그랬음..
'''
## 가중치별로 동일한 단어가 여러개이면 왼쪽인덱스 값 기준으로

def solution():
    N = int(input())
    value = [[] for _ in range(N)]
    words = []
    
    # 모든 단어를 위치 가중치별로 분류한다(오른쪽 인덱스 기준)
    for posPriority in range(N): 
        word = input()
        words.append(word)
        wordLength = len(word)
        for charIdx in range(wordLength): # charIdx는 0에 가까울 수록 가중치가 높은 것
            ## 분류할때 각단어별 왼쪽 인덱스 값도 함께 넣어준다
            value[posPriority].append((charIdx, word[charIdx]))

        value[posPriority] = sorted(value[posPriority], key=lambda x:x[0])

    # 알파벳 가중치 담긴 배열 alphaVal
    alphaVal = {}
    startVal = 10
    # 각 알파벳에 가중치에 따른 숫자를 부여한다
    ## value를 돌면서 해당 값이 숫자가 주어져 있으면 넘어간다.
    ## 숫자가 없으면 startVal + 1을 대입해 alphaVal에 추가해준다.
    for i in range(N):
        for charIdx, word in value[i]:
            try:
                if alphaVal[word]:
                    continue            
            except:
                if startVal != 0:
                    alphaVal[word] = startVal-1
        
    # 단어를 돌면서 해당문자를 숫자로 치환하고 새로운 숫자를 answer에 넣는다
    answer = []
    while words:
        word = list(words.pop(0))
        wordLength = len(word)
        tempWord =''
        for idx in range(wordLength):
            char = word[idx]
            number = alphaVal[char]
            tempWord += str(number)
        answer.append(int(tempWord))
    
    print(sum(answer))
solution()
        



        

    




