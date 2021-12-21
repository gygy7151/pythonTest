'''
'숫자카드게임'
숫자카드게임은 여러 숫자 카드중에서
가장 높은 숫자가 쓰인 카드

숫자가 쓰인 카드들은 N* M
N은 행의 개수
M은 열의개수

먼저 뽑고자 하는 카드가 포함되어 있는 행을 선택한다

그다음 선택된 행에 포함된 카드들중 가장
낮은 카드를 뽑아야 한다

처음에 카드를 골라낼 행을 선택할때
해당 행에서 가장 숫자가 낮은 카드를 뽑을 것을
고려하여

최종적으로 가장 높은 숫자의 카드를 뽑을 수 있도록 전략을
세워야 한다
'''

n, m= map(int, input().split())

'''
'''

def solution(n, m):

    # N*M 배열을 만들고
    arr = [[0] * m ] * n

    result = 0
    #원하는 숫자로 배열을 채워넣고
    for i in range(n):
        
        arr[i] = list(map(int, input().split()))
        
        for data in arr:
        #행의 요소중 가장 낮은 숫자요소를 고른다
            min_value = min(data)
        
        #이전 행의 낮은 숫자요소를 비교하여 더 큰 수를 결과값에 저장한다
        result = max(result, min_value)
        
    
    print(result)

solution(n, m)
