'''
분수찾기
'''
'''
두번째풀이
'''
X = int(input())
cnt = 1

if X != 1:

    while cnt < 5000:
        cnt += 1
        i = cnt - 1
        ### 예외처리 0보다 작은것만 하면 안됨. 0도 포함해야함
        if X - i <= 0:
            break
        
        #이러면 해당 idx부분의 몇번째 분수인지를 찾을 수 없음
        # elif X - i == 0:
        #     X -= i
        #     break

        else:
            X -= i

    idx = cnt - 1

else:
    idx = 1
print(idx)
print(X)
def solution(idx,option):
    temp_cnt = 0
    
    if option:
        
        for i in range(1,idx+1):
            
            for j in range(idx-i+1, idx-i,-1):

                temp_cnt += 1

                if X == 0:
                    print(str(i) + '/' + str(j))
                    return
                
                elif X == temp_cnt:
                    print(str(i) + '/' + str(j))
                    return
    
    else:
        
        for i in range(idx,0,-1):
        
            for j in range(idx-i+1, idx-i,-1):
                temp_cnt += 1
        
                if X == temp_cnt:
                    print(str(i) + '/' + str(j))
                    return

if idx == 1:
    print('1/1')

elif idx % 2 == 0:
    solution(idx,1)

else:
    solution(idx,0)




'''
첫번째풀이 - 시간초과
'''
# X = int(input())
# temp_cnt = 0
# cnt = 1

# def solution():
#     global temp_cnt
#     global cnt
#     while cnt < 5000:
#         for i in range(1,cnt+1):
#             for j in range(cnt-i+1,cnt-i,-1):
#                 temp_cnt+= 1
#                 if X == temp_cnt:
#                     print(str(i) + '/' + str(j))
#                     return
#         cnt += 1

# solution()
