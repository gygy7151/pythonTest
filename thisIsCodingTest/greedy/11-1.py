'''
모험가 길드

한마을에 모험가 N명이 있다.
모험가 길드에서 N명의 모험가를 대상으로 
'공포도'를 측정했다.
'공포도'높을수록 낮은 위험대처능력보유
공포도가 x인 모험가는 반드시 x명 이상
구성한 모험가 그룹에 참여해야 여행떠날 수 있음
=> 즉 같은 레벨끼리 묶음

동빈이는 n명의 모험가에 대한 정보가 주어졌을때
여행을 떠날 수 있는 그룹 수의 최댓갑을 구하는
프로그램을 작성.
'''

n = int(input())
adventors = list(input().split())



def findMax(num) :    

    for i in range(num) :

        max_value = max(adventors[i])

    if max_value == n :
        
        findMax(n-1)

result = findMax(n)


groupCount = 0
def findGroup(num) :
    global groupCount

    leftAdventors = num % int(result)

    if leftAdventors > 0:

        groupCount = leftAdventors + (num// int(result))
        findGroup(int(leftAdventors))
    
    else :
        print(groupCount)


findGroup(n)

