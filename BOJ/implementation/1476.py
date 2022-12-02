'''
날짜계산
'''
E, S, M = list(map(int, input().split(" ")))
answer = 1

while(True):
    if (answer - E) % 15 == 0 and (answer - S) % 28 == 0 and (answer - M) % 19 == 0 :
        print(answer)
        break
    else:
        answer+= 1
