'''
시각
정수 N이 입력되면 00시 00분 00초부터
N시 59분 59초까지 
모든 시각중에 3이 하나라도 포함되는 경우의수를 구함
'''

n = int(input())

def solution(n):
    count = 0
    #0시부터 N시까지
    for i in range(n+1) :
    
    #0분부터 59분까지
        for j in range(60) :

    #0초부터 59초까지
            for k in range(60) :
                times = str(i) + str(j) + str(k)
                
                for time in times:
                    if time == '3':
                        count += 1
                        break

    print(count)
    
solution(n)