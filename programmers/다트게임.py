'''
다트게임
'''
'''
세번째 풀이
'''
def solution(dartResult):
    answer = []
    # reaplce할때 새로운 객체를 기촌 dartResult가 참조하도록 반드시 주소참조해준다.
    dartResult = dartResult.replace('10', 'n')
    S = [ '10' if x == 'n' else x for x in dartResult]
    B = ['S', 'D', 'T']
    i = -1

    for s in S:
        if s in B:
            answer[i] = answer[i] ** (B.index(s)+1)
        #내가 문제를 잘못이해했다..
        elif s == '*':
            answer[i] = answer[i] * 2
            # 두번째
            if i != 0:
                answer[i-1] = answer[i-1]*2

        elif s == '#':
            answer[i] = answer[i] * (-1)
        
        else:
            answer.append(int(s))
            i += 1
    
    return sum(answer)

'''
두번째풀이 - 역시나 틀림..
'''
# def solution(dartResult):
#     answer = 0
#     S = []
#     B = {'S':1, 'D':2, 'T':3}

    
#     #문자열 3세트 구분
#     while len(dartResult) >= 4:
        
        
#         if dartResult[2] == '#' or dartResult[2] == '*':
#             S.append(dartResult[0:3])
#             dartResult = dartResult[3:]
#         elif dartResult[3] == '#' or dartResult[3] == '*':
#             S.append(dartResult[0:4])
#             dartResult = dartResult[4:]
              
#         else:
#             if dartResult[0:2] == '10':
#                 S.append(dartResult[0:3])
#                 dartResult = dartResult[3:]

#             else:
#                 S.append(dartResult[0:2])
#                 dartResult = dartResult[2:]

#     print(S)
#     print(dartResult) 
 
#     if len(dartResult) >= 2:
#         S.append(dartResult)
#     else:
#         S[-1] += dartResult 

#     # 옵션체킹
#     opt0_memo = [0,0,0]
#     opt1_memo = [0,0,0]
#     opt0_cnt = 0
#     opt1_cnt = 0
    
#     idx = 3
#     for s in S[-1::-1]:
#         idx -= 1

#         if s.count('*'):
#             opt0_cnt += 1
#             opt0_memo[idx] = opt0_cnt

#         if s.count('#'):
#             opt1_memo[idx] = 1
#             opt1_cnt += 1

#     print(len(S))
#     # 점수합계

#     for idx, s in enumerate(S): 

#         if s[0:2] != '10':
#             if opt0_memo[idx] >= 1 and opt1_memo[idx] == 0:
#                 answer += int(s[0])**B[s[1]] * (2 * opt0_memo[idx])
        
#             elif opt0_memo[idx] >= 1 and opt1_memo[idx] == 1:
#                 answer += int(s[0])**B[s[1]] * (-1) * (2 * opt0_memo[idx])
        

#             elif opt0_memo[idx] == 0 and opt1_memo[idx] == 0:
#                 answer += int(s[0])**B[s[1]]

#             else:
#                 answer += int(s[0])**B[s[1]] * (-1)
#         else:

#             if opt0_memo[idx] >= 1 and opt1_memo[idx] == 0:
#                 answer += int(s[0:2])**B[s[2]] * (2 * opt0_memo[idx])
        
#             elif opt0_memo[idx] >= 1 and opt1_memo[idx] == 1:
#                 answer += int(s[0:2])**B[s[2]] * (-1) * (2 * opt0_memo[idx])
        

#             elif opt0_memo[idx] == 0 and opt1_memo[idx] == 0:
#                 answer += int(s[0:2])**B[s[2]]

#             else:
#                 answer += int(s[0:2])**B[s[2]] * (-1)
            
   
#     return answer

'''
첫번째풀이
'''

# def solution(dartResult):
#     answer = 0
#     S = []
#     B = {'S':1, 'D':2, 'T':3}

    
#     #문자열 3세트 구분
#     while len(dartResult) >= 3:
        
        
#         if dartResult[2] == '#' or dartResult[2] == '*':
#             S.append(dartResult[0:3])
#             dartResult = dartResult[3:len(dartResult)]
        
#         else:
#             S.append(dartResult[0:2])
#             dartResult = dartResult[2:len(dartResult)]


#     if len(dartResult) == 2:
#         S.append(dartResult)
#     else:
#         S[-1] += dartResult 

#     # 옵션체킹
#     opt0_memo = [0,0,0]
#     opt1_memo = [0,0,0]
#     opt0_cnt = 0
#     opt1_cnt = 0
    
#     idx = 3
#     for s in S[-1::-1]:
#         idx -= 1

#         if s.count('*'):
#             opt0_cnt += 1
#             opt0_memo[idx] = opt0_cnt

#         if s.count('#'):
#             opt1_memo[idx] = 1
#             opt1_cnt += 1

#     # 점수합계
#     print(S)
#     for idx, s in enumerate(S): 


#         if opt0_memo[idx] >= 1 and opt1_memo[idx] == 0:
#             answer += int(s[0])**B[s[1]] * (2 * opt0_memo[idx])
        
#         elif opt0_memo[idx] >= 1 and opt1_memo[idx] == 1:
#             answer += int(s[0])**B[s[1]] * (-1) * (2 * opt0_memo[idx])
        

#         elif opt0_memo[idx] == 0 and opt1_memo[idx] == 0:
#             print(s[0])
#             print(s[1])
#             answer += int(s[0])**B[s[1]]

#         else:
#             answer += int(s[0])**B[s[1]] * (-1)
        
#     return answer

A = '10S2D*10D*'
print(solution(A))