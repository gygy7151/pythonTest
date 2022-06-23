'''
곱셈
'''
'''
세번째풀이 - 제발 주석처리좀 잘하자..
'''
zero =  ''
A = list(input())[-1::-1]
B = list(input())[-1::-1]
for i in range(len(A)):
    A[i] = int(A[i] + zero)
    B[i] = int(B[i] + zero)
    zero += '0'
# print(A,B)

answer = 0
for idx, b in enumerate(B):
    res = 0
    for a in A:
        res += a*b
    answer += res
    res = str(res)
    print(res[0:len(res)-idx])
print(answer)

'''
두번째풀이  - 틀림
'''
# A = list(input())[-1::-1]
# B = list(input())[-1::-1]
# answer = 0
# b_zero = ''
# for b in B:
#     res = 0
#     a_zero = ''
#     for a in A:
#         print(int(str(int(b)*int(a)) + a_zero + b_zero))
#         res += int(str(int(b)*int(a)) + a_zero + b_zero)
        
#         a_zero += '0'
#     b_zero += '0'
#     answer += res
    # print(answer)

'''
첫번째풀이 - 틀림
'''
# A = sorted(list(input()), reverse=True)
# B = sorted(list(input()), reverse=True)
# for b in B:
#     answer = 0
#     for a in A:
#         answer += int(b)*int(a)
#     print(answer)